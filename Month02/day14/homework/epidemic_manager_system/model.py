class EpidemicModel:
    """
        疫情模型：包装疫情信息
    """

    def __init__(self, region="", new=0, now=0, total=0, eid=0):
        self.region = region
        self.new = new
        self.now = now
        self.total = total
        self.eid = eid

    def __str__(self):
        return "%s地区编号是%s,新增%s人,现有%s人,累计%s人" % (self.region, self.eid, self.new, self.now, self.total)

    def __eq__(self, other): 
        return self.eid == other
