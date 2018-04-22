# coding: utf-8

from jqdata.apis import (
    balance,
    cash_flow,
    income,
    indicator,
    valuation,
    bank_indicator,
    security_indicator,
    insurance_indicator
)


finance = {
    # 市值数据
    'capitalization': valuation.capitalization,
    'circulating_cap': valuation.circulating_cap,
    'market_cap': valuation.market_cap,
    'circulating_market_cap': valuation.circulating_market_cap,
    'turnover_ratio': valuation.turnover_ratio,
    'pe_ratio': valuation.pe_ratio,
    'pe_ratio_lyr': valuation.pe_ratio_lyr,
    'pb_ratio': valuation.pb_ratio,
    'ps_ratio': valuation.ps_ratio,
    'pcf_ratio': valuation.pcf_ratio,

    # 资产负债数据
    'cash_equivalents': balance.cash_equivalents,
    'settlement_provi': balance.settlement_provi,
    'lend_capital': balance.lend_capital,
    'trading_assets': balance.trading_assets,
    'bill_receivable': balance.bill_receivable,
    'account_receivable': balance.account_receivable,
    'advance_payment': balance.advance_payment,
    'insurance_receivables': balance.insurance_receivables,
    'reinsurance_receivables': balance.reinsurance_receivables,
    'reinsurance_contract_reserves_receivable': balance.reinsurance_contract_reserves_receivable,
    'interest_receivable': balance.interest_receivable,
    'dividend_receivable': balance.dividend_receivable,
    'other_receivable': balance.other_receivable,
    'bought_sellback_assets': balance.bought_sellback_assets,
    'inventories': balance.inventories,
    'non_current_asset_in_one_year': balance.non_current_asset_in_one_year,
    'other_current_assets': balance.other_current_assets,
    'total_current_assets': balance.total_current_assets,
    'loan_and_advance': balance.loan_and_advance,
    'hold_for_sale_assets': balance.hold_for_sale_assets,
    'hold_to_maturity_investments': balance.hold_to_maturity_investments,
    'longterm_receivable_account': balance.longterm_receivable_account,
    'longterm_equity_invest': balance.longterm_equity_invest,
    'investment_property': balance.investment_property,
    'fixed_assets': balance.fixed_assets,
    'constru_in_process': balance.constru_in_process,
    'construction_materials': balance.construction_materials,
    'fixed_assets_liquidation': balance.fixed_assets_liquidation,
    'biological_assets': balance.biological_assets,
    'oil_gas_assets': balance.oil_gas_assets,
    'intangible_assets': balance.intangible_assets,
    'development_expenditure': balance.development_expenditure,
    'good_will': balance.good_will,
    'long_deferred_expense': balance.long_deferred_expense,
    'deferred_tax_assets': balance.deferred_tax_assets,
    'other_non_current_assets': balance.other_non_current_assets,
    'total_non_current_assets': balance.total_non_current_assets,
    'total_assets': balance.total_assets,
    'shortterm_loan': balance.shortterm_loan,
    'borrowing_from_centralbank': balance.borrowing_from_centralbank,
    'deposit_in_interbank': balance.deposit_in_interbank,
    'borrowing_capital': balance.borrowing_capital,
    'trading_liability': balance.trading_liability,
    'notes_payable': balance.notes_payable,
    'accounts_payable': balance.accounts_payable,
    'advance_peceipts': balance.advance_peceipts,
    'sold_buyback_secu_proceeds': balance.sold_buyback_secu_proceeds,
    'commission_payable': balance.commission_payable,
    'salaries_payable': balance.salaries_payable,
    'taxs_payable': balance.taxs_payable,
    'interest_payable': balance.interest_payable,
    'dividend_payable': balance.dividend_payable,
    'other_payable': balance.other_payable,
    'reinsurance_payables': balance.reinsurance_payables,
    'insurance_contract_reserves': balance.insurance_contract_reserves,
    'proxy_secu_proceeds': balance.proxy_secu_proceeds,
    'receivings_from_vicariously_sold_securities': balance.receivings_from_vicariously_sold_securities,
    'non_current_liability_in_one_year': balance.non_current_liability_in_one_year,
    'other_current_liability': balance.other_current_liability,
    'total_current_liability': balance.total_current_liability,
    'longterm_loan': balance.longterm_loan,
    'bonds_payable': balance.bonds_payable,
    'longterm_account_payable': balance.longterm_account_payable,
    'specific_account_payable': balance.specific_account_payable,
    'estimate_liability': balance.estimate_liability,
    'deferred_tax_liability': balance.deferred_tax_liability,
    'other_non_current_liability': balance.other_non_current_liability,
    'total_non_current_liability': balance.total_non_current_liability,
    'total_liability': balance.total_liability,
    'paidin_capital': balance.paidin_capital,
    'capital_reserve_fund': balance.capital_reserve_fund,
    'treasury_stock': balance.treasury_stock,
    'specific_reserves': balance.specific_reserves,
    'surplus_reserve_fund': balance.surplus_reserve_fund,
    'ordinary_risk_reserve_fund': balance.ordinary_risk_reserve_fund,
    'retained_profit': balance.retained_profit,
    'foreign_currency_report_conv_diff': balance.foreign_currency_report_conv_diff,
    'equities_parent_company_owners': balance.equities_parent_company_owners,
    'minority_interests': balance.minority_interests,
    'total_owner_equities': balance.total_owner_equities,
    'total_sheet_owner_equities': balance.total_sheet_owner_equities,

    # 现金流数据
    'goods_sale_and_service_render_cash': cash_flow.goods_sale_and_service_render_cash,
    'net_deposit_increase': cash_flow.net_deposit_increase,
    'net_borrowing_from_central_bank': cash_flow.net_borrowing_from_central_bank,
    'net_borrowing_from_finance_co': cash_flow.net_borrowing_from_finance_co,
    'net_original_insurance_cash': cash_flow.net_original_insurance_cash,
    'net_cash_received_from_reinsurance_business': cash_flow.net_cash_received_from_reinsurance_business,
    'net_insurer_deposit_investment': cash_flow.net_insurer_deposit_investment,
    'net_deal_trading_assets': cash_flow.net_deal_trading_assets,
    'interest_and_commission_cashin': cash_flow.interest_and_commission_cashin,
    'net_increase_in_placements': cash_flow.net_increase_in_placements,
    'net_buyback': cash_flow.net_buyback,
    'tax_levy_refund': cash_flow.tax_levy_refund,
    'other_cashin_related_operate': cash_flow.other_cashin_related_operate,
    'subtotal_operate_cash_inflow': cash_flow.subtotal_operate_cash_inflow,
    'goods_and_services_cash_paid': cash_flow.goods_and_services_cash_paid,
    'net_loan_and_advance_increase': cash_flow.net_loan_and_advance_increase,
    'net_deposit_in_cb_and_ib': cash_flow.net_deposit_in_cb_and_ib,
    'original_compensation_paid': cash_flow.original_compensation_paid,
    'handling_charges_and_commission': cash_flow.handling_charges_and_commission,
    'policy_dividend_cash_paid': cash_flow.policy_dividend_cash_paid,
    'staff_behalf_paid': cash_flow.staff_behalf_paid,
    'tax_payments': cash_flow.tax_payments,
    'other_operate_cash_paid': cash_flow.other_operate_cash_paid,
    'subtotal_operate_cash_outflow': cash_flow.subtotal_operate_cash_outflow,
    'net_operate_cash_flow': cash_flow.net_operate_cash_flow,
    'invest_withdrawal_cash': cash_flow.invest_withdrawal_cash,
    'invest_proceeds': cash_flow.invest_proceeds,
    'fix_intan_other_asset_dispo_cash': cash_flow.fix_intan_other_asset_dispo_cash,
    'net_cash_deal_subcompany': cash_flow.net_cash_deal_subcompany,
    'other_cash_from_invest_act': cash_flow.other_cash_from_invest_act,
    'subtotal_invest_cash_inflow': cash_flow.subtotal_invest_cash_inflow,
    'fix_intan_other_asset_acqui_cash': cash_flow.fix_intan_other_asset_acqui_cash,
    'invest_cash_paid': cash_flow.invest_cash_paid,
    'impawned_loan_net_increase': cash_flow.impawned_loan_net_increase,
    'net_cash_from_sub_company': cash_flow.net_cash_from_sub_company,
    'other_cash_to_invest_act': cash_flow.other_cash_to_invest_act,
    'subtotal_invest_cash_outflow': cash_flow.subtotal_invest_cash_outflow,
    'net_invest_cash_flow': cash_flow.net_invest_cash_flow,
    'cash_from_invest': cash_flow.cash_from_invest,
    'cash_from_mino_s_invest_sub': cash_flow.cash_from_mino_s_invest_sub,
    'cash_from_borrowing': cash_flow.cash_from_borrowing,
    'cash_from_bonds_issue': cash_flow.cash_from_bonds_issue,
    'other_finance_act_cash': cash_flow.other_finance_act_cash,
    'subtotal_finance_cash_inflow': cash_flow.subtotal_finance_cash_inflow,
    'borrowing_repayment': cash_flow.borrowing_repayment,
    'dividend_interest_payment': cash_flow.dividend_interest_payment,
    'proceeds_from_sub_to_mino_s': cash_flow.proceeds_from_sub_to_mino_s,
    'other_finance_act_payment': cash_flow.other_finance_act_payment,
    'subtotal_finance_cash_outflow': cash_flow.subtotal_finance_cash_outflow,
    'net_finance_cash_flow': cash_flow.net_finance_cash_flow,
    'exchange_rate_change_effect': cash_flow.exchange_rate_change_effect,
    'cash_equivalent_increase': cash_flow.cash_equivalent_increase,
    'cash_equivalents_at_beginning': cash_flow.cash_equivalents_at_beginning,
    'cash_and_equivalents_at_end': cash_flow.cash_and_equivalents_at_end,

    # 利润数据
    'total_operating_revenue': income.total_operating_revenue,
    'operating_revenue': income.operating_revenue,
    'interest_income': income.interest_income,
    'premiums_earned': income.premiums_earned,
    'commission_income': income.commission_income,
    'total_operating_cost': income.total_operating_cost,
    'operating_cost': income.operating_cost,
    'interest_expense': income.interest_expense,
    'commission_expense': income.commission_expense,
    'refunded_premiums': income.refunded_premiums,
    'net_pay_insurance_claims': income.net_pay_insurance_claims,
    'withdraw_insurance_contract_reserve': income.withdraw_insurance_contract_reserve,
    'policy_dividend_payout': income.policy_dividend_payout,
    'reinsurance_cost': income.reinsurance_cost,
    'operating_tax_surcharges': income.operating_tax_surcharges,
    'sale_expense': income.sale_expense,
    'administration_expense': income.administration_expense,
    'financial_expense': income.financial_expense,
    'asset_impairment_loss': income.asset_impairment_loss,
    'fair_value_variable_income': income.fair_value_variable_income,
    'investment_income': income.investment_income,
    'invest_income_associates': income.invest_income_associates,
    'exchange_income': income.exchange_income,
    'operating_profit': income.operating_profit,  # dup
    'non_operating_revenue': income.non_operating_revenue,
    'non_operating_expense': income.non_operating_expense,
    'disposal_loss_non_current_liability': income.disposal_loss_non_current_liability,
    'total_profit': income.total_profit,
    'income_tax_expense': income.income_tax_expense,
    'net_profit': income.net_profit,
    'np_parent_company_owners': income.np_parent_company_owners,
    'minority_profit': income.minority_profit,
    'basic_eps': income.basic_eps,
    'diluted_eps': income.diluted_eps,
    'other_composite_income': income.other_composite_income,
    'total_composite_income': income.total_composite_income,
    'ci_parent_company_owners': income.ci_parent_company_owners,
    'ci_minority_owners': income.ci_minority_owners,

    # 财务指标数据
    'eps': indicator.eps,
    'adjusted_profit': indicator.adjusted_profit,
    'operating_profit': indicator.operating_profit,  # dup
    'value_change_profit': indicator.value_change_profit,
    'roe': indicator.roe,
    'inc_return': indicator.inc_return,
    'roa': indicator.roa,
    'net_profit_margin': indicator.net_profit_margin,
    'gross_profit_margin': indicator.gross_profit_margin,
    'expense_to_total_revenue': indicator.expense_to_total_revenue,
    'operation_profit_to_total_revenue': indicator.operation_profit_to_total_revenue,
    'net_profit_to_total_revenue': indicator.net_profit_to_total_revenue,
    'operating_expense_to_total_revenue': indicator.operating_expense_to_total_revenue,
    'ga_expense_to_total_revenue': indicator.ga_expense_to_total_revenue,
    'financing_expense_to_total_revenue': indicator.financing_expense_to_total_revenue,
    'operating_profit_to_profit': indicator.operating_profit_to_profit,
    'invesment_profit_to_profit': indicator.invesment_profit_to_profit,
    'adjusted_profit_to_profit': indicator.adjusted_profit_to_profit,
    'goods_sale_and_service_to_revenue': indicator.goods_sale_and_service_to_revenue,
    'ocf_to_revenue': indicator.ocf_to_revenue,
    'ocf_to_operating_profit': indicator.ocf_to_operating_profit,
    'inc_total_revenue_year_on_year': indicator.inc_total_revenue_year_on_year,
    'inc_total_revenue_annual': indicator.inc_total_revenue_annual,
    'inc_revenue_year_on_year': indicator.inc_revenue_year_on_year,
    'inc_revenue_annual': indicator.inc_revenue_annual,
    'inc_operation_profit_year_on_year': indicator.inc_operation_profit_year_on_year,
    'inc_operation_profit_annual': indicator.inc_operation_profit_annual,
    'inc_net_profit_year_on_year': indicator.inc_net_profit_year_on_year,
    'inc_net_profit_annual': indicator.inc_net_profit_annual,
    'inc_net_profit_to_shareholders_year_on_year': indicator.inc_net_profit_to_shareholders_year_on_year,
    'inc_net_profit_to_shareholders_annual': indicator.inc_net_profit_to_shareholders_annual,

    # 银行业专项指标
    'total_loan': bank_indicator.total_loan,
    'total_deposit': bank_indicator.total_deposit,
    'interest_earning_assets': bank_indicator.interest_earning_assets,
    'non_interest_earning_assets': bank_indicator.non_interest_earning_assets,
    'interest_earning_assets_yield': bank_indicator.interest_earning_assets_yield,
    'interest_bearing_liabilities': bank_indicator.interest_bearing_liabilities,
    'non_interest_bearing_liabilities': bank_indicator.non_interest_bearing_liabilities,
    'interest_bearing_liabilities_interest_rate': bank_indicator.interest_bearing_liabilities_interest_rate,
    'non_interest_income': bank_indicator.non_interest_income,
    'non_interest_income_ratio': bank_indicator.non_interest_income_ratio,
    'net_interest_margin': bank_indicator.net_interest_margin,
    'net_profit_margin': bank_indicator.net_profit_margin,
    'core_level_capital': bank_indicator.core_level_capital,
    'net_core_level_capital': bank_indicator.net_core_level_capital,
    'core_level_capital_adequacy_ratio': bank_indicator.core_level_capital_adequacy_ratio,
    'net_level_1_capital': bank_indicator.net_level_1_capital,
    'level_1_capital_adequacy_ratio': bank_indicator.level_1_capital_adequacy_ratio,
    'net_capital': bank_indicator.net_capital,
    'capital_adequacy_ratio': bank_indicator.capital_adequacy_ratio,
    'weighted_risky_asset': bank_indicator.weighted_risky_asset,
    'deposit_loan_ratio': bank_indicator.deposit_loan_ratio,
    'short_term_asset_liquidity_ratio_CNY': bank_indicator.short_term_asset_liquidity_ratio_CNY,
    'short_term_asset_liquidity_ratio_FC': bank_indicator.short_term_asset_liquidity_ratio_FC,
    'Nonperforming_loan_rate': bank_indicator.Nonperforming_loan_rate,
    'single_largest_customer_loan_ratio': bank_indicator.single_largest_customer_loan_ratio,
    'top_ten_customer_loan_ratio': bank_indicator.top_ten_customer_loan_ratio,
    'bad_debts_reserve': bank_indicator.bad_debts_reserve,
    'non_performing_loan_provision_coverage': bank_indicator.non_performing_loan_provision_coverage,
    'cost_to_income_ratio': bank_indicator.cost_to_income_ratio,
    'former_core_capital': bank_indicator.former_core_capital,
    'former_net_core_capital': bank_indicator.former_net_core_capital,
    'former_net_core_capital_adequacy_ratio': bank_indicator.former_net_core_capital_adequacy_ratio,
    'former_net_capital': bank_indicator.former_net_capital,
    'former_capital_adequacy_ratio': bank_indicator.former_capital_adequacy_ratio,
    'former_weighted_risky_asset': bank_indicator.former_weighted_risky_asset,
    'normal_amount': bank_indicator.normal_amount,
    'normal_amount_ratio': bank_indicator.normal_amount_ratio,
    'concerned_amount': bank_indicator.concerned_amount,
    'concerned_amount_ratio': bank_indicator.concerned_amount_ratio,
    'secondary_amount': bank_indicator.secondary_amount,
    'secondary_amount_ratio': bank_indicator.secondary_amount_ratio,
    'suspicious_amount': bank_indicator.suspicious_amount,
    'suspicious_amount_ratio': bank_indicator.suspicious_amount_ratio,
    'loss_amount': bank_indicator.loss_amount,
    'loss_amount_ratio': bank_indicator.loss_amount_ratio,
    'short_term_loan_average_balance': bank_indicator.short_term_loan_average_balance,
    'short_term_loan_annualized_average_interest_rate': bank_indicator.short_term_loan_annualized_average_interest_rate,
    'mid_term_loan_annualized_average_balance': bank_indicator.mid_term_loan_annualized_average_balance,
    'mid_term_loan_annualized_average_interest_rate': bank_indicator.mid_term_loan_annualized_average_interest_rate,
    'enterprise_deposits_average_balance': bank_indicator.enterprise_deposits_average_balance,
    'enterprise_deposits_average_interest_rate': bank_indicator.enterprise_deposits_average_interest_rate,
    'savings_deposit_average_balance': bank_indicator.savings_deposit_average_balance,
    'savings_deposit_average_interest_rate': bank_indicator.savings_deposit_average_interest_rate,

    # 券商专项指标
    'net_capital': security_indicator.net_capital,
    'net_assets': security_indicator.net_assets,
    'net_capital_to_reserve': security_indicator.net_capital_to_reserve,
    'net_capital_to_net_asset': security_indicator.net_capital_to_net_asset,
    'net_capital_to_debt': security_indicator.net_capital_to_debt,
    'net_asset_to_debt': security_indicator.net_asset_to_debt,
    'net_capital_to_sales_department_number': security_indicator.net_capital_to_sales_department_number,
    'own_stock_to_net_capital': security_indicator.own_stock_to_net_capital,
    'own_security_to_net_capital': security_indicator.own_security_to_net_capital,
    'operational_risk_reserve': security_indicator.operational_risk_reserve,
    'broker_risk_reserve': security_indicator.broker_risk_reserve,
    'own_security_risk_reserve': security_indicator.own_security_risk_reserve,
    'security_underwriting_reserve': security_indicator.security_underwriting_reserve,
    'asset_management_reserve': security_indicator.asset_management_reserve,
    'own_equity_derivatives_to_net_capital': security_indicator.own_equity_derivatives_to_net_capital,
    'own_fixed_income_to_net_capital': security_indicator.own_fixed_income_to_net_capital,
    'margin_trading_reserve': security_indicator.margin_trading_reserve,
    'branch_risk_reserve': security_indicator.branch_risk_reserve,

    # 保险专项指标
    'investment_assets': insurance_indicator.investment_assets,
    'total_investment_rate_of_return': insurance_indicator.total_investment_rate_of_return,
    'net_investment_rate_of_return': insurance_indicator.net_investment_rate_of_return,
    'earned_premium': insurance_indicator.earned_premium,
    'earned_premium_growth_rate': insurance_indicator.earned_premium_growth_rate,
    'payoff_cost': insurance_indicator.payoff_cost,
    'compensation_rate': insurance_indicator.compensation_rate,
    'not_expired_duty_reserve': insurance_indicator.not_expired_duty_reserve,
    'outstanding_claims_reserve': insurance_indicator.outstanding_claims_reserve,
    'comprehensive_cost_ratio': insurance_indicator.comprehensive_cost_ratio,
    'comprehensive_compensation_rate': insurance_indicator.comprehensive_compensation_rate,
    'solvency_adequacy_ratio': insurance_indicator.solvency_adequacy_ratio,
    'actual_capital': insurance_indicator.actual_capital,
    'minimum_capital': insurance_indicator.minimum_capital,
}