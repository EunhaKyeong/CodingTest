/*
https://school.programmers.co.kr/learn/courses/30/lessons/42840
 */

class Solution {
    private val soopoja1: IntArray = intArrayOf(1, 2, 3, 4, 5)
    private val soopoja2: IntArray = intArrayOf(2, 1, 2, 3, 2, 4, 2, 5)
    private val soopoja3: IntArray = intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    
    fun solution(answers: IntArray): IntArray {
        var answer = intArrayOf()
        
        val soopoja1AnswerCnt: Int = answers.filterIndexed{ index, value -> value==soopoja1[index % soopoja1.size] }.size
        val soopoja2AnswerCnt: Int = answers.filterIndexed{ index, value -> value==soopoja2[index % soopoja2.size] }.size
        val soopoja3AnswerCnt: Int = answers.filterIndexed{ index, value -> value==soopoja3[index % soopoja3.size] }.size
        
        val answerHm = mutableMapOf(1 to soopoja1AnswerCnt, 2 to soopoja2AnswerCnt, 3 to soopoja3AnswerCnt)
        answer = answerHm.filterValues {it==answerHm.values.maxOrNull()}.keys.toMutableList().sorted().toIntArray()
        
        return answer
    }
}