from stripe import util
from stripe.six.moves.urllib.parse import quote_plus



def patch_custom_methods(cls, custom_resources):
    for resource in custom_resources:
        http_verb = resource["http_verb"]

        if http_verb not in ["get", "post", "delete"]:
            raise ValueError(
                "Invalid http_verb: %s. Must be one of 'get', 'post' or 'delete'"
                % http_verb
            )

        name = resource["name"]
        http_path = resource.get("http_path", name)

        # move the actual pathing to a separate function
        # to avoid "Late binding closures".
        # See: https://docs.python-guide.org/writing/gotchas/#late-binding-closures
        _patch(cls=cls, name=name, http_verb=http_verb, http_path=http_path)


def _patch(cls, name, http_verb, http_path):
    async def custom_method_request(cls, sid, **params):
        url = "%s/%s/%s" % (
            cls.class_url(),
            quote_plus(util.utf8(sid)),
            http_path,
        )
        return await cls._static_request(http_verb, url, **params)

    existing_method = getattr(cls, name, None)
    if existing_method is None:
        setattr(cls, name, classmethod(custom_method_request))
    else:
        # If a method with the same name we want to use already exists on
        # the class, we assume it's an instance method. In this case, the
        # new class method is prefixed with `_cls_`, and the original
        # instance method is decorated with `util.class_method_variant` so
        # that the new class method is called when the original method is
        # called as a class method.
        setattr(cls, "_cls_" + name, classmethod(custom_method_request))
        instance_method = util.class_method_variant("_cls_" + name)(
            existing_method
        )
        setattr(cls, name, instance_method)