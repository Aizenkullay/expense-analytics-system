import datetime
import pandas as pd
import matplotlib.pyplot as plt
from modules.utils import line
from modules.file_handler import load_data
def analysis():

    expenses = load_data()
    if len(expenses) == 0:
        print("No entries to analyze !")
        return
    
    date=datetime.datetime.now()
    dtime=date.strftime("%d-%m-%Y_%H-%M")
    
    category_tools = {}
    
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category not in category_tools:
            category_tools[category] = amount
        else:
            category_tools[category] += amount
    
    df = pd.DataFrame(list(category_tools.items()), columns=['category', 'amount'])
    
    avg_by_category = df["amount"].mean()
    minimum = df["amount"].min()
    maximum = df['amount'].max()
    
    total_amount = 0
    for total in expenses:
        total_amount += total['amount']
    
    avg_per_expense = total_amount / len(expenses)
    
    print("=" * 50)
    print("ANALYSIS SUMMARY")
    print("=" * 50)
    print(f"💰 Total (from expenses):   ₹{total_amount:,.2f}")
    print(f"📈 Average per category:    ₹{avg_by_category:,.2f}")
    print(f"📈 Average per expense:     ₹{avg_per_expense :,.2f}")
    print(f"📉 Minimum category total:  ₹{minimum:,.2f}")
    print(f"📈 Maximum category total:  ₹{maximum:,.2f}")
    print(f"📊 Number of categories:    {len(df)}")
    print(f"📝 Number of expenses:      {len(expenses)}")
    print("=" * 50)
    
    plt.figure(figsize=(10, 6))
    df = df.sort_values('amount', ascending=True)
    
    bars = plt.barh(df['category'], df['amount'], color='#2f12bb', alpha=0.752)
    
    for bar in bars:
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height() / 2, f' ₹{width:,.0f}', 
                 ha='left', va='center', fontsize=9)
    
    plt.title("Expense Analysis by Category", fontsize=14, fontweight='bold')
    plt.xlabel("AMOUNT", fontsize=11)
    plt.ylabel("Categories", fontsize=11)
    plt.savefig(f"exports/charts/complete_analysis_{dtime}.png")
    df.to_csv(f"exports/csv/analysis_{dtime}.csv")
    plt.show()
    plt.close()


def monthly_analysis():
    
    expenses=load_data()
    date=datetime.datetime.now()
    dtime=date.strftime("%d-%m-%Y_%H-%M")
    if len(expenses)==0:
        print("No data found")
        return
    df_expenses=pd.DataFrame(expenses)
    df_expenses['user_date']=pd.to_datetime(df_expenses["user_date"],format="%d-%m-%Y")
    df_expenses['month']=df_expenses["user_date"].dt.strftime("%Y-%m")
    monthly_totals=df_expenses.groupby('month')['amount'].sum()

    print("\nMONTHLY EXPENSE SUMMARY")

    for month,total in monthly_totals.items():
        print(f"{month} : ₹{total:,.2f}")
    
    plt.figure(figsize=(8,6))
    plt.plot(monthly_totals,color="#11a21f",alpha=0.752)
    plt.scatter(monthly_totals.index, monthly_totals.values, 
            color="#ac0c0c", s=100 , zorder=5, edgecolor='white', linewidth=2)
    for month, amount in monthly_totals.items():
        plt.annotate(f'₹{amount:,.0f}', 
                 xy=(month, amount),
                 xytext=(0, 10), 
                 textcoords='offset points',
                 ha='center', 
                 fontsize=9)
    plt.title("Monthly analysis",fontsize=14,fontweight='bold')
    plt.xlabel("Month",fontweight='bold')
    plt.ylabel("Amount spent in ₹",fontweight='bold')
    plt.grid(True)
    plt.savefig(f"exports/charts/monthly_trend_{dtime}.png")
    monthly_totals.to_csv(f"exports/csv/monthly_csv/monthly_analysis_{dtime}.csv")
    plt.show()
    plt.close()