def main():
    # Get the number of years
    num_years = int(input("Enter the number of years: "))

    # Initialize total rainfall
    total_rainfall = 0

    # Iterate over each year
    for year in range(1, num_years + 1):
        print(f"Year {year}:")
        for month in range(1, 13):
            rainfall = float(input(f"Enter rainfall (in inches) for month {month}: "))
            total_rainfall += rainfall

    # Calculate the total number of months
    num_months = num_years * 12

    # Calculate average rainfall
    average_rainfall = total_rainfall / num_months

    # Display results
    print(f"\nTotal months: {num_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f} inches")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

if __name__ == "__main__":
    main()
