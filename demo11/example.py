# 初始化函数，设定基准等等
def initialize(context):
    # 设定基准
    # set_benchmark("600000.XSHG")
    set_benchmark("000300.XSHG")
    g.security = "000001.XSHE"

    # 每天10点
    # run_daily(market_open, time="10:00", reference_security="000300.XSHG")
    # 每分钟
    # run_daily(market_open, time="every_bar", reference_security="000300.XSHG")

    run_daily(market_open, time="9:30")
    run_daily(after_market_close, time="15:30")

    # 每月第一天
    # run_monthly(market_open, 1, time="open")

    # 每周每周最后一天
    # run_weekly(market_open, -1, time="open")

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
    # 充值10000
    inout_cash(10000, pindex=0)

    log.info("可用资金: {}".format(context.portfolio.subportfolios[0].available_cash))

    # 获取账户的所有现金
    # cash = context.portfolio.available_cash

    # 没有持仓
    if g.security not in context.portfolio.positions:
        # 全仓买入
        # order_value(g.security, cash)
        # 下单1000股
        order(g.security, 1000)
    else:
        # 全仓卖出
        # order_target(g.security, 0)
        # 卖出500股
        order(g.security, -500)


def after_market_close(context):
    # 获取所有当天未完成订单
    orders = get_open_orders()

    for _order in orders:
        log.info("未完成订单: {}".format(_order))

    # 撤单
    for _order in orders:
        log.info("撤单: {}".format(_order))
        cancel_order(_order)
