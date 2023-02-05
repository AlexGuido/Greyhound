/*Fibonacci*/
fun main(args: Array<String>){
    var a:Int = 0; var b:Int = 1; var c:Int = a + b;  var n:Int = 18

    println(a)
    println(b)
    println(c)
    for(i in 1..18) {
        a = b; b = c; c = a + b
        println(c)
    }
}