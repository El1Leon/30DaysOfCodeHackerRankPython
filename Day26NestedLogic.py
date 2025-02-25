# Function to calculate library fine
def calculate_fine(d1, m1, y1, d2, m2, y2):
    # If the book is returned on or before the expected return date
    if y1 < y2 or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 <= d2):
        return 0
    
    # If the book is returned after the expected return year
    if y1 > y2:
        return 10000
    
    # If the book is returned after the expected return month but in the same year
    if m1 > m2 and y1 == y2:
        return 500 * (m1 - m2)
    
    # If the book is returned after the expected return day but in the same month and year
    if d1 > d2 and m1 == m2 and y1 == y2:
        return 15 * (d1 - d2)

# Input handling
if __name__ == '__main__':
    # Read the actual return date
    d1, m1, y1 = map(int, input().split())  
    # Read the expected return date
    d2, m2, y2 = map(int, input().split())
    
    # Calculate the fine
    fine = calculate_fine(d1, m1, y1, d2, m2, y2)
    
    # Print the fine
    print(fine)
