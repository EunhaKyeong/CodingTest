/*
https://school.programmers.co.kr/learn/courses/30/lessons/134240
 */

class Solution {
    fun solution(food: IntArray): String {
        var answer: String = ""
        
        for (i in 1 until food.size) {
            answer += i.toString().repeat(food[i] / 2)
        }
        
        answer += "0"
        answer += answer.substring(0, answer.length-1).reversed()
        
        return answer
    }
}