# Class that provides test data with unique values
class TestDataUniqueValues:
    
    # Static method that returns an array with unique values
    @staticmethod
    def get_array():
        # Returns an array with two unique values, [1, 2]
        return [x for x in range(1, 3)]
    
    # Static method that returns the expected index of the minimum value in the array
    @staticmethod
    def get_expected_result():
        # Since the smallest value is 1 at index 0, the expected result is 0
        return 0

# Class that provides test data with exactly two different minimum values
class TestDataExactlyTwoDifferentMinimums:
    
    # Static method that returns an array where two values are the same minimum
    @staticmethod
    def get_array():
        # Returns an array with two minimum values 1 and a larger number 3, [1, 1, 3]
        return [1, 1, 3]
    
    # Static method that returns the expected index of the first occurrence of the minimum value
    @staticmethod
    def get_expected_result():
        # The smallest value is 1, and the first occurrence is at index 0, so the expected result is 0
        return 0

# Class that provides test data for an empty array
class TestDataEmptyArray:
    
    # Static method that returns an empty array
    @staticmethod
    def get_array():
        # Returns an empty array, []
        return []
