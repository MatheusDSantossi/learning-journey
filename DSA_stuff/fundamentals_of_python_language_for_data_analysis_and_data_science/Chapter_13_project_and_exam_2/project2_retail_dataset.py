import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("dados/dataset.csv");

# print(df[df["Cidade"] == "New York City"])

print("Which city has the biggest products sale value from the 'Office Supplies' category?")
print("------------------------")

office_suplies_df = df[df["Categoria"] == 'Office Supplies']

sale_values = office_suplies_df[["Valor_Venda", "Categoria", "Cidade"]]

cities_summed = sale_values.groupby("Cidade")["Valor_Venda"].sum().idxmax()

print(cities_summed)

# print(sale_values.groupby("Cidade")["Valor_Venda"].sum())

print("What's the total of sales by Order Date -> Year?")
print("OBS: Show the result using a bar chart!")
print("------------------------")

df["Data_Pedido"] = pd.to_datetime(df["Data_Pedido"], format="mixed")
df.set_index('Data_Pedido', inplace=True)

# Month
# sales_by_order_date = df["Valor_Venda"].resample("M").max()
# Year
sales_by_order_date = df["Valor_Venda"].resample("Y").max()

# sales_by_order_date.plot(kind='bar', figsize=(10, 6))
# plt.xlabel("Date")
# plt.ylabel("Maximum Sales")
# plt.title("Maximum Sales by Date")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

print("What's the total of sales by state?")
print("OBS: Show the result using a bar chart!")
print("------------------------")

total_of_sale_by_state = df.groupby("Estado")["Valor_Venda"].sum()

# total_of_sale_by_state.plot(kind="bar", figsize=(10, 6))
# plt.xlabel("State")
# plt.ylabel("Sales")
# plt.title("Total of sales by state")
# plt.show()

print("What's the 10 cities with the biggest total of sales?")
print("OBS: Show the result using a bar chart!")
print("------------------------")

total_sales_by_city = df.groupby("Cidade")["Valor_Venda"].sum().sort_values(ascending=False).head(10)

print(total_sales_by_city)

# total_sales_by_city.plot(kind="bar", figsize=(10, 6))
# plt.xlabel("Cities")
# plt.ylabel("Sales")
# plt.title("The 10 biggest Sales Cities")
# plt.show()

print("Which segment had the biggest Total of Sale?")
print("OBS: Show the result using a pie chart!")
print("------------------------")

# A simple function to transform the value into a percentage
def absolute_value(val):
    a = np.round(val / 100 * df.groupby("Segmento")["Valor_Venda"].sum(), 0)
    return a

biggest_total_sales_segment = df.groupby("Segmento")["Valor_Venda"].sum().sort_values(ascending=False)

biggest_total_sales_segment.plot(kind="pie", figsize=(10, 6))
# plt.pie(biggest_total_sales_segment, autopct=absolute_value)
# plt.xlabel("Segments")
# plt.legend(biggest_total_sales_segment.index.astype(str))
# plt.va
# plt.show()

print("(Baby level) What the Total of Sales by segment and Year?")
print("------------------------")


# ============================================
# SOLUTION
# ============================================

def analyze_sales_by_segment_and_year(df):
    """Answer: Total Sales by Segment and Year"""
    
    # Prepare the data
    df_copy = df.copy()
    df_copy["Data_Pedido"] = pd.to_datetime(df_copy["Data_Pedido"], format="mixed")
    df_copy['Year'] = df_copy['Data_Pedido'].dt.year
    
    # Group by both Segment and Year
    sales_by_segment_year = df_copy.groupby(['Segmento', 'Year'])['Valor_Venda'].sum().unstack(fill_value=0)
    
    print("📊 TOTAL SALES BY SEGMENT AND YEAR:")
    print("=" * 50)
    print(sales_by_segment_year.round(2))
    
    return sales_by_segment_year

# ============================================
# VISUALIZATION 1: GROUPED BAR CHART (CORRECT VERSION)
# ============================================

def create_grouped_bar_chart(sales_by_segment_year):
    """Create a proper grouped bar chart"""
    
    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Get data
    segments = sales_by_segment_year.index
    years = sales_by_segment_year.columns
    
    # Set up bar positions
    x = np.arange(len(segments))
    width = 0.2  # Width of bars
    
    # Create bars for each year
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFD700']
    
    for i, year in enumerate(years):
        values = sales_by_segment_year[year].values
        bars = ax.bar(x + i * width, values, width, 
                     label=str(year), color=colors[i % len(colors)], alpha=0.8)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'${height:,.0f}',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3),  # 3 points vertical offset
                       textcoords="offset points",
                       ha='center', va='bottom', fontsize=9, rotation=45)
    
    # Customize the chart
    ax.set_xlabel('Segment', fontsize=12, fontweight='bold')
    ax.set_ylabel('Total Sales ($)', fontsize=12, fontweight='bold')
    ax.set_title('Total Sales by Segment and Year', fontsize=14, fontweight='bold')
    ax.set_xticks(x + width * (len(years) - 1) / 2)
    ax.set_xticklabels(segments)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    # Format y-axis to show values in thousands/millions
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
    
    plt.tight_layout()
    plt.show()

# ============================================
# VISUALIZATION 2: STACKED BAR CHART
# ============================================

def create_stacked_bar_chart(sales_by_segment_year):
    """Create a stacked bar chart showing year over year"""
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Transpose for stacked bars by year
    data_transposed = sales_by_segment_year.T
    
    # Create stacked bars
    data_transposed.plot(kind='bar', stacked=True, ax=ax, 
                        colormap='Set3', alpha=0.8)
    
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Total Sales ($)', fontsize=12, fontweight='bold')
    ax.set_title('Total Sales by Year (Stacked by Segment)', fontsize=14, fontweight='bold')
    ax.legend(title='Segment', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(axis='y', alpha=0.3)
    
    # Format y-axis
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ============================================
# VISUALIZATION 4: LINE CHART FOR TRENDS
# ============================================

def create_trend_analysis(sales_by_segment_year):
    """Show trends over time for each segment"""
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plot lines for each segment
    for segment in sales_by_segment_year.index:
        values = sales_by_segment_year.loc[segment]
        ax.plot(values.index, values.values, marker='o', linewidth=3, 
                label=segment, markersize=8)
        
        # Add value labels
        for x, y in zip(values.index, values.values):
            ax.annotate(f'${y:,.0f}', (x, y), textcoords="offset points", 
                       xytext=(0,10), ha='center', fontsize=9)
    
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Total Sales ($)', fontsize=12, fontweight='bold')
    ax.set_title('Sales Trends by Segment Over Time', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Format y-axis
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
    
    plt.tight_layout()
    plt.show()

# ============================================
# COMPLETE ANALYSIS FUNCTION
# ============================================

def complete_sales_analysis(df):
    """Run complete analysis"""
    
    print("🎯 ANALYZING SALES BY SEGMENT AND YEAR")
    print("=" * 60)
    
    # Get the cross-tabulation
    sales_by_segment_year = analyze_sales_by_segment_and_year(df)
    
    # Create visualizations
    print("\n📊 Creating Grouped Bar Chart...")
    create_grouped_bar_chart(sales_by_segment_year)
    
    print("\n📊 Creating Stacked Bar Chart...")
    create_stacked_bar_chart(sales_by_segment_year)

    
    print("\n📊 Creating Trend Analysis...")
    create_trend_analysis(sales_by_segment_year)
    
    # Summary insights
    print("\n💡 KEY INSIGHTS:")
    print("-" * 30)
    
    # Best performing segment overall
    total_by_segment = sales_by_segment_year.sum(axis=1)
    best_segment = total_by_segment.idxmax()
    print(f"🏆 Best performing segment: {best_segment} (${total_by_segment[best_segment]:,.0f})")
    
    # Best performing year
    total_by_year = sales_by_segment_year.sum(axis=0)
    best_year = total_by_year.idxmax()
    print(f"📈 Best performing year: {best_year} (${total_by_year[best_year]:,.0f})")
    
    # Growth rates
    print(f"\n📊 Year-over-Year Growth:")
    for segment in sales_by_segment_year.index:
        first_year = sales_by_segment_year.loc[segment].iloc[0]
        last_year = sales_by_segment_year.loc[segment].iloc[-1]
        growth_rate = ((last_year - first_year) / first_year) * 100
        print(f"   {segment}: {growth_rate:.1f}%")

# ============================================
# FIXED VERSION OF YOUR CODE
# ============================================

def your_code_fixed(df):
    """This is how your code should look"""
    
    # Prepare data
    df_copy = df.copy()
    df_copy["Data_Pedido"] = pd.to_datetime(df_copy["Data_Pedido"], format="mixed")
    df_copy['Year'] = df_copy['Data_Pedido'].dt.year
    
    # Get sales by segment and year
    sales_by_segment_year = df_copy.groupby(['Segmento', 'Year'])['Valor_Venda'].sum().unstack(fill_value=0)
    
    # Create the grouped bar chart
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Bar settings
    segments = sales_by_segment_year.index
    years = sales_by_segment_year.columns
    x = np.arange(len(segments))
    width = 0.2
    
    # Create bars for each year
    for i, year in enumerate(years):
        ax.bar(x + i * width, sales_by_segment_year[year], width, label=str(year))
    
    ax.set_xlabel('Segment')
    ax.set_ylabel('Total Sales ($)')
    ax.set_title('Total Sales by Segment and Year')
    ax.set_xticks(x + width * (len(years) - 1) / 2)
    ax.set_xticklabels(segments)
    ax.legend()
    
    plt.tight_layout()
    plt.show()

# Running the complete analysis
complete_sales_analysis(df)
