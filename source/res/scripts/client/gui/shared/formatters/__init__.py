# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/shared/formatters/__init__.py
import BigWorld
from debug_utils import LOG_ERROR
from gui.shared.formatters import icons
from gui.shared.formatters import text_styles
from gui.shared.formatters import time_formatters
from gui.shared.formatters.currency import getBWFormatter
from gui.shared.gui_items import GUI_ITEM_ECONOMY_CODE
from gui.shared.money import Money, Currency
from helpers.i18n import makeString
__all__ = ('icons', 'text_styles', 'time_formatters')

def formatPrice(price, reverse=False, defaultCurrency=Currency.CREDITS):
    outPrice = []
    currencies = price.getSetCurrencies(byWeight=False)
    if not currencies:
        currencies = [defaultCurrency]
    for currency in currencies:
        formatter = getBWFormatter(currency)
        cname = makeString('#menu:price/{}'.format(currency)) + ': '
        value = price.get(currency, 0)
        cformatted = formatter(value) if formatter else value
        outPrice.append(''.join((cformatted, ' ', cname) if reverse else (cname, ' ', cformatted)))

    return ', '.join(outPrice)


def formatPriceForCurrency(money, currencyName):
    return formatPrice(Money(money.get(currencyName)))


def formatGoldPrice(gold, reverse=False):
    return formatPrice(Money(gold=gold), reverse, defaultCurrency=Currency.GOLD)


def getGlobalRatingFmt(globalRating):
    return BigWorld.wg_getIntegralFormat(globalRating) if globalRating >= 0 else '--'


def moneyWithIcon(money, currType=None):
    if currType is None:
        currType = money.getCurrency()
    style = getattr(text_styles, currType)
    icon = getattr(icons, currType)
    value = money.get(currType)
    formatter = getBWFormatter(currType)
    if style is not None and icon is not None and value is not None:
        return style(formatter(value)) + icon()
    else:
        LOG_ERROR('Unsupported currency for displaying with icon:', currType)
        return formatter(value)


def getMoneyVO(moneyObj):
    return tuple(((c, v) for c, v in moneyObj.iteritems()))


def getMoneyVOWithReason(errorMsg, moneyObj):
    result = []
    for c, v in moneyObj.iteritems():
        if errorMsg == GUI_ITEM_ECONOMY_CODE.getMoneyError(c):
            result.append(('%sError' % c, v))
        result.append((c, v))

    return tuple(result)


def getItemPricesVO(*itemPrices):
    resultVO = []
    for itemPrice in itemPrices:
        action = itemPrice.getActionPrcAsMoney()
        if action.isDefined():
            vo = {'price': getMoneyVO(itemPrice.price),
             'defPrice': getMoneyVO(itemPrice.defPrice),
             'action': getMoneyVO(action)}
            resultVO.append(vo)
        resultVO.append({'price': getMoneyVO(itemPrice.price)})

    return resultVO


def getItemPricesVOWithReason(reason, *itemPrices):
    resultVO = []
    for itemPrice in itemPrices:
        action = itemPrice.getActionPrcAsMoney()
        if action.isDefined():
            vo = {'price': getMoneyVOWithReason(reason, itemPrice.price),
             'defPrice': getMoneyVO(itemPrice.defPrice),
             'action': getMoneyVO(action)}
            resultVO.append(vo)
        resultVO.append({'price': getMoneyVOWithReason(reason, itemPrice.price)})

    return resultVO
