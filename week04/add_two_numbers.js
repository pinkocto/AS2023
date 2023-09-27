function doSomething() {
//document는 html파일을 말하고, element는 태그라고 생각// 태그 중 Id를 찾아서 value값을 a라고 함.
    let a = document.getElementById('inputA').value;
    let b = document.getElementById('inputB').value;
    document.getElementById("valueA").innerHTML = a;
    document.getElementById("valueB").innerHTML = b;
    document.getElementById("valueC").innerHTML = Number(a) + Number(b);
}