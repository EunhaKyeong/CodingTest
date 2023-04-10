/*
https://school.programmers.co.kr/learn/courses/30/lessons/42889
 */
 
class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        var answer = intArrayOf()
        var failRateMap: MutableMap<Int, Double> = mutableMapOf<Int, Double>()
        
        for (n in 1 .. N) {
            if (stages.filter{ it==n }.size==0) {
                failRateMap.put(n, 0.0)
            } else {
                failRateMap.put(n, stages.filter{ it==n }.size.toDouble() / stages.filter{ it >= n }.size.toDouble())
            }
        }
        
        answer = failRateMap.toList().sortedByDescending { it.second }.toMap().keys.toIntArray()
        
        return answer
    }
}