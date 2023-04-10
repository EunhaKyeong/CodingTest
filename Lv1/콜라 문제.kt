/*
https://school.programmers.co.kr/learn/courses/30/lessons/132267
 */

class Solution {
    private var acquired: Int = 0
    private var remained: Int = 0
    
    fun solution(a: Int, b: Int, n: Int): Int {
        var answer: Int = 0
        
        remained = n
        while (remained >= a) {
            acquired = remained / a * b
            remained = remained % a + acquired
            answer += acquired
        }
        
        return answer
    }
}