/*
https://school.programmers.co.kr/learn/courses/30/lessons/12977
 */

class Solution {
    fun solution(nums: IntArray): Int {
        var answer = 0
 
        for (i in 0 until nums.size - 2) {
            for (j in i+1 until nums.size - 1) {
                for (k in j+1 until nums.size) {
                    val finalNum = nums.get(i) + nums.get(j) + nums.get(k)
                    
                    if ((2..Math.sqrt(finalNum.toDouble()).toInt()).none { finalNum % it == 0 })
                        answer ++
                }
            }
        }

        return answer
    }
}