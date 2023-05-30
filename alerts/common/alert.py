class Alert(object):
    def __init__(self,
                 price,
                 created_by,
                 status,
                 is_active,
                 **kwargs):
        self.price = price
        self.created_by = created_by
        self.status = status
        self.is_active = is_active