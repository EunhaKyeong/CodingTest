/*
https://school.programmers.co.kr/learn/courses/30/lessons/120876
*/

class Solution {
    fun solution(lines: Array<IntArray>): Int {
        var answer: Int = 0
        
        val line1Dots: List<Int> = getLineElement(lines[0])
        val line2Dots: List<Int> = getLineElement(lines[1])
        val line3Dots: List<Int> = getLineElement(lines[2])
        
        val line12Dots = line1Dots.intersect(line2Dots)
        val line23Dots = line2Dots.intersect(line3Dots)
        val line13Dots = line1Dots.intersect(line3Dots)
        
        answer = line12Dots.union(line23Dots).union(line13Dots).distinct().size
        
        return answer
    }
    
    private fun getLineElement(line: IntArray): List<Int> {
        var list: ArrayList<Int> = arrayListOf()
        
        for (i in line[0] until line[1]) {
            list.add(i)
        }
        
        return list.toList()
    }
}