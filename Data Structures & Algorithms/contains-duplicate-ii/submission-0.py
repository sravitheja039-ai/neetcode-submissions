class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        h = {}

        for i in range(len(nums)):

            if nums[i] in h:
                # check distance between current index and previous index
                if i - h[nums[i]] <= k:
                    return True

            # store/update latest index
            h[nums[i]] = i

        return False