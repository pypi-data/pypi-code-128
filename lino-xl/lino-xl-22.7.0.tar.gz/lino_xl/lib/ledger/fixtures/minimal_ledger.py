# -*- coding: UTF-8 -*-
# Copyright 2012-2022 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

from lino.api import dd, rt, _
from lino_xl.lib.ledger.choicelists import DC, CommonAccounts
# from lino.utils import Cycler

vat = dd.resolve_app('vat')
sales = dd.resolve_app('sales')
ledger = dd.resolve_app('ledger')
finan = dd.resolve_app('finan')
bevat = dd.resolve_app('bevat')
eevat = dd.resolve_app('eevat')
bevats = dd.resolve_app('bevats')
#~ partners = dd.resolve_app('partners')
has_payment_methods = dd.get_plugin_setting('ledger', 'has_payment_methods', False)


def objects():

    JournalGroups = rt.models.ledger.JournalGroups
    Company = rt.models.contacts.Company

    # JOURNALS

    kw = dict(journal_group=JournalGroups.sales)
    if sales:
        # MODEL = sales.VatProductInvoice
        MODEL = sales.InvoicesByJournal
    else:
        MODEL = vat.VatAccountInvoice
    kw.update(trade_type='sales')
    # kw.update(ref="OFF", dc=DC.credit)
    # kw.update(printed_name=_("Offer"))
    # kw.update(dd.str2kw('name', _("Offers")))
    # yield MODEL.create_journal(**kw)

    kw.update(ref="SLS", dc=DC.credit)
    kw.update(dd.str2kw('printed_name', _("Invoice")))
    # kw.update(dd.str2kw('name', _("Sales invoices")))
    # kw.update(printed_name=_("Invoice"))
    kw.update(dd.str2kw('name', _("Sales invoices")))
    SLS_JOURNAL = MODEL.create_journal(**kw)
    yield SLS_JOURNAL

    # if dd.is_installed('invoicing') and dd.plugins.invoicing.delivery_notes_demo:
    # stories_journal = dd.plugins.ledger.sales_stories_journal
    sales_method = dd.plugins.ledger.sales_method
    if sales_method and sales_method != 'direct':
        misc_partner = rt.models.contacts.Company(
            name="Miscellaneous",
            country=dd.plugins.countries.get_my_country())
        yield misc_partner
        kw.update(partner=misc_partner)
        if sales_method == "delivery":
            kw.update(ref="SDN", dc=DC.credit)
            kw.update(dd.str2kw('printed_name', _("Delivery note")))
            kw.update(dd.str2kw('name', _("Delivery notes")))
            kw.update(make_ledger_movements=False)
        elif sales_method == "pos":
            kw.update(ref="SSN", dc=DC.credit)
            kw.update(dd.str2kw('printed_name', _("Sales note")))
            kw.update(dd.str2kw('name', _("Sales notes")))
            kw.update(make_ledger_movements=True)
        else:
            raise Exception("Unsupported sales method {}".format(sales_method))
        SDN_JOURNAL = sales.CashInvoicesByJournal.create_journal(**kw)
        yield SDN_JOURNAL
        yield rt.models.invoicing.FollowUpRule(
            source_journal=SDN_JOURNAL,
            target_journal=SLS_JOURNAL)
        # yield PaymentMethod(designation=_("Cash payment"), journal=SDN_JOURNAL)

    if has_payment_methods:

        PaymentMethod = rt.models.ledger.PaymentMethod

        def payment_method(designation, payment_account, **kwargs):
            if payment_account:
                kwargs.update(payment_account=CommonAccounts.get_by_name(
                    payment_account).get_object())
            # kwargs.update(journal=SLS_JOURNAL)
            return PaymentMethod(**dd.str2kw('designation', designation, **kwargs))

        yield payment_method(_("Cash payment"), "cash", is_cash=True)
        yield payment_method(_("PayPal"), "online_payments")
        yield payment_method(_("bKash"), "online_payments")
        # yield payment_method(_("Cash on delivery"), "cash")

    if dd.plugins.vat.declaration_plugin is None:
        dd.logger.warning("No journal SLC, BNK, PMO etc because declaration_plugin is None")
        return

    kw.update(ref="SLC", dc=DC.debit)
    kw.update(dd.str2kw('name', _("Sales credit notes")))
    kw.update(dd.str2kw('printed_name', _("Credit note")))
    yield MODEL.create_journal(**kw)

    kw.update(journal_group=JournalGroups.purchases)
    kw.update(trade_type='purchases', ref="PRC")
    kw.update(dd.str2kw('name', _("Purchase invoices")))
    kw.update(dd.str2kw('printed_name', _("Invoice")))
    kw.update(dc=DC.debit)
    if dd.is_installed('ana'):
        yield rt.models.ana.AnaAccountInvoice.create_journal(**kw)
    else:
        yield vat.VatAccountInvoice.create_journal(**kw)

    if finan:

        bestbank = Company(
            name="Bestbank",
            country=dd.plugins.countries.get_my_country())
        yield bestbank

        kw = dict(journal_group=JournalGroups.financial)
        kw.update(dd.str2kw('name', _("Bestbank Payment Orders")))
        kw.update(dd.str2kw('printed_name', _("Payment order")))
        # kw.update(dd.babel_values(
        #     'name', de="Zahlungsaufträge", fr="Ordres de paiement",
        #     en="Payment Orders", et="Maksekorraldused"))
        kw.update(
            trade_type='bank_po',
            partner=bestbank,
            account=CommonAccounts.pending_po.get_object(),
            ref="PMO")
        kw.update(dc=DC.credit)  # 20201219  PMO Journal.dc
        yield finan.PaymentOrder.create_journal(**kw)

        kw = dict(journal_group=JournalGroups.financial)
        # kw.update(trade_type='')
        kw.update(dc=DC.credit)
        kw.update(account=CommonAccounts.cash.get_object(), ref="CSH")
        kw.update(dd.str2kw('name', _("Cash book")))
        kw.update(dd.str2kw('printed_name', _("Cash statement")))
        yield finan.BankStatement.create_journal(**kw)

        kw.update(dd.str2kw('name', _("Bestbank")))
        kw.update(dd.str2kw('printed_name', _("Bank statement")))
        kw.update(account=CommonAccounts.best_bank.get_object(), ref="BNK")
        kw.update(dc=DC.credit)
        yield finan.BankStatement.create_journal(**kw)

        kw.update(journal_group=JournalGroups.misc)
        kw.update(account=CommonAccounts.cash.get_object(), ref="MSC")
        # kw.update(dc=DC.credit)
        kw.update(dd.str2kw('name', _("Miscellaneous transactions")))
        kw.update(dd.str2kw('printed_name', _("Transaction")))
        yield finan.JournalEntry.create_journal(**kw)

        kw.update(preliminary=True, ref="PRE")
        kw.update(dd.str2kw('name', _("Preliminary transactions")))
        yield finan.JournalEntry.create_journal(**kw)

        kw = dict(journal_group=JournalGroups.wages)
        kw.update(dd.str2kw('name', _("Paychecks")))
        kw.update(dd.str2kw('printed_name', _("Paycheck")))
        kw.update(account=CommonAccounts.cash.get_object(), ref="SAL")
        kw.update(dc=DC.debit)
        yield finan.JournalEntry.create_journal(**kw)



    for m in (bevat, bevats, eevat):
        if not m:
            continue
        kw = dict(journal_group=JournalGroups.vat)
        kw.update(trade_type='taxes')
        kw.update(dd.str2kw('name', _("VAT declarations")))
        kw.update(dd.str2kw('printed_name', _("VAT declaration")))
        kw.update(must_declare=False)
        kw.update(account=CommonAccounts.due_taxes.get_object())
        kw.update(ref=m.DEMO_JOURNAL_NAME, dc=DC.debit)
        yield m.Declaration.create_journal(**kw)

    payments = []
    if finan:
        payments += [finan.BankStatement, finan.JournalEntry,
                     finan.PaymentOrder]

    pending_po = CommonAccounts.pending_po.get_object()
    wages = CommonAccounts.wages.get_object()
    tax_offices = CommonAccounts.tax_offices.get_object()

    MatchRule = rt.models.ledger.MatchRule
    for jnl in ledger.Journal.objects.all():
        if jnl.voucher_type.model in payments:
            yield MatchRule(
                journal=jnl,
                account=CommonAccounts.customers.get_object())
            yield MatchRule(
                journal=jnl,
                account=CommonAccounts.suppliers.get_object())
            if tax_offices:
                yield MatchRule(journal=jnl, account=tax_offices)
            if wages:
                yield MatchRule(journal=jnl, account=wages)
            if jnl.voucher_type.model is not finan.PaymentOrder:
                if pending_po:
                    yield MatchRule(journal=jnl, account=pending_po)
        elif jnl.trade_type:
            a = jnl.trade_type.get_main_account()
            if a:
                yield MatchRule(journal=jnl, account=a)
        # if jnl.voucher_type.model in payments:

    # pending_po = CommonAccounts.pending_po.get_object()
    # if pending_po:
    #     for jnl in ledger.Journal.objects.filter(voucher_type__in=VoucherTypes.finan.BankStatement):
    #         yield MatchRule(journal=jnl, account=pending_po)
