mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

# TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
# for loop start
weekly_sales = 0
for side in [mon_sales, tues_sales, wed_sales, thurs_sales, fri_sales]:
    side = int(side)
    weekly_sales = side + weekly_sales
    # for loop end
weekly_sales = str(weekly_sales)  # controvert to string
print("This week's total sales: " + weekly_sales)

# or you can write
# weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
