import fix_yahoo_finance as yf
import datetime
import pickle

class DataBroker:
    def __init__(self, start_date=datetime.date(2000, 1, 1)):
        self.data = {}
        self.load_data()
        self.start_date = start_date
        self.today = datetime.datetime.now().date() - datetime.timedelta(days=1)
         
    # Reads the pickle file and initiate the data dictionary.
    def load_data(self):
        try:
            self.data = pickle.load(open("data_store.p", "rb"))
        except FileNotFoundError:
            print("No data was found")
            return False
        print(self.data.keys())
        return True
          
    # Write data to the pickle file.
    def save_data(self):
        pickle.dump(self.data, open("data_store.p", "wb"))
        return True
    
    # Updates data for every company to the last day of trading
    def update_all_companies(self):
        for company in self.data.keys():
            self.update_company(company)
        return True
        
    # Updates a the date of a company, if no data exists adds the company to the database. 
    def update_company(self, company):        
        if company in self.data.keys():      
            cur_date = self.data[company].index.max().date()
            diff = (self.today - cur_date).days
            if diff > 0 and diff < 3 and datetime.date.today().weekday() >= 5:
                return True
            elif diff > 0:
                append_data = yf.download([company], start=cur_date, end=self.today)
                self.data[company].append(append_data)
        else:
            self.data[company] = yf.download([company], start=self.start_date, end=self.today)
        self.save_data()
        return True
    
    # Returns the data of collected on a company
    def load_company(self, company, start_date=None, end_date=None):
        if not start_date:
            start_date = self.start_date
        if not end_date: 
            end_date = self.today
        return self.data[company][start_date:end_date]
    
    # Clears the database and overwrites the data-file.
    def clear_database(self):
        self.data = {}
        self.save_data()
        return True
    
    def get_all_company_data(self, company):
        return self.data[company]
    
    # Returns the "Opening" price for a specific company at a specific date. If no date provided, last day of trading will be used
    def get_company_stock_price(self, company, date):
        if not date:
            return self.data[company]["Open"][-1]
        date_index = self.data[company]["Open"].index.get_loc(date, method='pad')
        return self.data[company]["Open"][date_index]