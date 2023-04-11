/*
https://school.programmers.co.kr/learn/courses/30/lessons/120956
*/

lass Solution {
    fun solution(babbling: Array<String>): Int {
        var answer: Int = 0
        
        for (b in babbling) {
            if (check(b))
                answer++
        }
        
        return answer
    }
    
    private fun check(b: String): Boolean {   
        val words = b.split("aya", "ye", "woo", "ma")
        return words.all { it.isBlank() }
    }
}