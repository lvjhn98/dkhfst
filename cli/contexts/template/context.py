

def create(parser):
    from .actions.var import action
    action(parser)
    
    from .actions.up import action
    action(parser)

    from .actions.down import action
    action(parser)

    from .actions.logs import action
    action(parser)

    from .actions.ip_list import action
    action(parser)
    
    from .actions.ip_of import action
    action(parser)
    
    from .actions.dns_entries import action
    action(parser)

    from .actions.dns_publish import action
    action(parser)

    from .actions.dns_refresh import action
    action(parser)
    
    from .actions.dns_connect import action
    action(parser)

    from .actions.get_ca import action
    action(parser)

    from .actions.dns_update import action
    action(parser)

