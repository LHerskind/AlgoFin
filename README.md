# AlgoFin


## TODO:
* data:
  * actions = (Trader_name_and_params, start_funds, start_date, end_date, [action], [company])
    * action = (buy|sell|none, company, price, amount)
* simulate_trader(Trader, [company], start_date, end_date, start_funds, profit_only=False) returns (profit, actions)
  * Additional flags to return profit only
* simulate_traders([Trader], [company], start_date, end_date, start_funds) returns profit
* Visualize:
  * visualize_profits([actions], relative=False) returns plots
  * visualize_balances([actions], relative=False) returns plot
  * visualize_buy_and_sells(actions) returns plot
* Trader (class):
  * data:
    * date, balance, data
  * constructor(start_date, start_funds, data)
  * set_date(date)
  * predict(date,[,])
  * next() returns action
* Data_broker (class):
  * dict[company, data]:
  * save to and load from file
  * append to existing data
  * update_all_companies(date)
  * update_company(company)
  * load_company(company, start_date=, end_date=) return data
