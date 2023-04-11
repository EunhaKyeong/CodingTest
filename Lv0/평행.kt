/*
https://school.programmers.co.kr/learn/courses/30/lessons/120875
*/

class Solution {
    fun solution(dots: Array<IntArray>): Int {        
        //dots[0], dots[1] | dots[2], dots[3]  기울기 계산
        if (getScope(dots[0], dots[1])==getScope(dots[2], dots[3]))
            return 1
        else {  //dots[0], dots[3] | dots[1], dots[2] 기울기 계산
            if (getScope(dots[0], dots[3])==getScope(dots[1], dots[2]))
                return 1
            else 
                return 0
        }    
    }
    
    private fun getScope(dot1: IntArray, dot2: IntArray): Float {
        return (dot2[0] - dot1[0]).toFloat() / (dot2[1] - dot1[1]).toFloat()
    }
}