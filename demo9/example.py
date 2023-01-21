# 初始化函数，设定基准等等
def initialize(context):
    # 设定基准
    # set_benchmark("600000.XSHG")
    set_benchmark("000300.XSHG")
    g.security = "000001.XSHE"
    run_daily(market_open, time="10:00")
    # 佣金 & 印花税
    # set_order_cost(
    #     OrderCost(
    #         open_commission=0.03,
    #         close_commission=0.03,
    #         close_tax=0.001,
    #         min_commission=5
    #         ),
    #         type='stock'
    #     )
    # 滑点
    # set_slippage(PriceRelatedSlippage(0.002), type="stock")
    # 成交量
    # set_option("order_volume_ratio", 0.5)
    # 复权
    set_option("use_real_price", True)


## 开盘时运行函数
def market_open(context):
    if g.security not in context.portfolio.positions:
        order(g.security, 1000)
    else:
        order(g.security, -800)
