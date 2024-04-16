import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Data analysis project - 2016 BC housing affordability and rental subsidies
#Name :Chanpreet Kaur
#Date :10-April-2024

# Load the dataset

data = pd.read_csv("BC census 2016 data.csv")

while True:
    print("\nMenu:")
    print("1. Task 1: CHSAs with shelt_rent_30plus_rate > 50%")
    print("2. Task 2: Mean shelter subsidization rates across PHA regions")
    print("3. Correlation Matrix")
    print("4. Income vs Rent Price")
    print("5. Shelter Rent Subsidized Rate Across PHA Regions")
    print("6. Population vs Rent Burden Rate")
    print("7. Median Rent Price and Income Across PHA Regions")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice == '1':
        # Task 1: Identify CHSAs where shelt_rent_30plus_rate > 50%
        
        highRentChsas = data[data['shelt_rent_30plus_rate'] > 50]
        high_burden_areas_count = highRentChsas.shape[0]
        avg_income_high_burden = highRentChsas['income_total_mean'].mean()
        avg_rent_high_burden = highRentChsas['shelt_rent_mo_cost_mean'].mean()
        subsidization_appropriate = "appropriate" if avg_income_high_burden > avg_rent_high_burden else "inappropriate"
        print("\nTask 1: CHSAs with shelt_rent_30plus_rate > 50%")
        print(f"Number of CHSAs with shelt_rent_30plus_rate > 50%: {high_burden_areas_count}")
        print(f"Average Household Income in high burden areas: ${avg_income_high_burden:.2f}")
        print(f"Average Rent Price in high burden areas: ${avg_rent_high_burden:.2f}")
        print(f"Considering the household income and rent prices, the rental subsidization rates of these areas are {subsidization_appropriate}.")
        #display Graph
        plt.figure(figsize=(10, 6))
        plt.bar(highRentChsas['chsa'], highRentChsas['shelt_rent_30plus_rate'], color='orange')
        plt.title('CHSAs with Shelter Rent 30%+ Rate > 50%')
        plt.xlabel('Community Health Service Areas (CHSA)')
        plt.ylabel('Spending 30% or more of their income Shelter Rent 30%+ Rate (%)')
        plt.xticks(rotation=90)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()
    
    elif choice == '2':
        # Task 2: Compare shelter subsidization rates across PHA regions
        try:
        
            pha_regions = ['Fraser', 'Interior', 'Northern', 'Vancouver Coastal', 'Vancouver Island']
            mean_subsidization_rates = data.groupby('pha')['shelt_rent_30plus_rate'].mean().loc[pha_regions]
            #display Graph
            plt.figure(figsize=(12, 6))
            sns.barplot(x=mean_subsidization_rates.index, y=mean_subsidization_rates.values, palette='viridis')
            plt.xlabel('PHA Regions')
            plt.ylabel('Mean Shelter Subsidization Rate (%)')
            plt.title('Mean Shelter Subsidization Rates across PHA Regions')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except RuntimeWarning:
            print("")
    
    elif choice == '3':
        # Correlation Analysis
        correlation_matrix = data[['shelt_rent_30plus_rate', 'income_total_mean', 'shelt_rent_mo_cost_mean']].corr()
        plt.figure(figsize=(10, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.show()
    
    elif choice == '4':
        # Income vs Rent Price
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='income_total_mean', y='shelt_rent_mo_cost_mean', data=data, marker='o', markersize=8)
        plt.xlabel('Mean Household Income')
        plt.ylabel('Mean Rent Price')
        plt.title('Income vs Rent Price')
        plt.grid(True)
        #display Graph
        plt.show()
    
    elif choice == '5':
        # Shelter Rent Subsidized Rate Across PHA Regions
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='pha', y='shelt_rent_subsidized_rate', data=data)
        plt.xlabel('PHA Regions')
        plt.ylabel('Shelter Rent Subsidized Rate (%)')
        plt.title('Shelter Rent Subsidized Rate Across PHA Regions')
        plt.xticks(rotation=45)
        plt.show()
    
    elif choice == '6':
        # Population vs Rent Burden Rate
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='chsa_population_census', y='shelt_rent_30plus_rate', data=data)
        plt.xlabel('CHSA Population')
        plt.ylabel('Rent Burden Rate (%)')
        plt.title('Population vs Rent Burden Rate')
        #display Graph
        plt.show()
    
    elif choice == '7':
        # Median Rent Price and Income Across PHA Regions
        pha_region_comparison = data.groupby('pha')[['shelt_rent_mo_cost_mean', 'income_total_mean']].median().loc[pha_regions]
        plt.figure(figsize=(12, 6))
        pha_region_comparison.plot(kind='bar')
        plt.xlabel('PHA Regions')
        plt.ylabel('Median Value')
        plt.title('Median Rent Price and Income Across PHA Regions')
        plt.xticks(rotation=45)
        plt.tight_layout()
        #display Graph
        plt.show()
    
    elif choice == '8':
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")

