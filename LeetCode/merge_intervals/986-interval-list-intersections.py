# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a_i = 0
        b_i = 0
        out = []
        
        if not firstList or not secondList:
            return out
        
        # manually add an 'end' for the while loop to compare against
        end = max(firstList[-1][1], secondList[-1][1]) + 1
        firstList.append([end, end])
        secondList.append([end, end])

        while a_i < len(firstList) - 1 and b_i < len(secondList) - 1:
            overlap = [-1, -1]
            inc_ai = inc_bi = False
            
            if firstList[a_i][0] >= secondList[b_i][0] and \
               firstList[a_i][0] <= secondList[b_i][1]:
                overlap = [firstList[a_i][0], min(firstList[a_i][1], secondList[b_i][1])]
                
            elif secondList[b_i][0] >= firstList[a_i][0] and \
                 secondList[b_i][0] <= firstList[a_i][1]:
                overlap = [secondList[b_i][0], min(firstList[a_i][1], secondList[b_i][1])]
            
            if overlap[0] >= 0 and overlap[1] >= 0:
                out.append(overlap)
            
            if firstList[a_i + 1][0] > secondList[b_i][1]:
                inc_bi = True
            if secondList[b_i + 1][0] > firstList[a_i][1]:
                inc_ai = True
            
            if inc_ai:
                a_i += 1
            if inc_bi:
                b_i += 1
        
        return out
