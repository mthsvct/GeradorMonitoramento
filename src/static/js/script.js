function outrosPeriodos(op){
    if(op == 0){
        document.getElementById("DatasPersonalizadas").style.display = "flex";
    } else {
        document.getElementById("DatasPersonalizadas").style.display = "none";
    }
}

function pegaMinimo() {
    let inicial = document.getElementById('dataInicial');
    let final = document.getElementById('inputDataFinal');
    final.min = inicial.value
}


function insereValorMinutagem(op) {
    let a = document.getElementById('inputMin');
    let u = parseInt(op)
    a.value = u
}

function apresenteTalMenu(op) {
    if(op == 4) {
        document.getElementById("selRequisitos").style.display = "flex";
        document.getElementById("selMS").style.display = "none";
    } 
    
    if(op == 5) {
        document.getElementById("selRequisitos").style.display = "none";
        document.getElementById("selMS").style.display = "flex";
    }
    
    if( op < 4 ) {
        document.getElementById("selRequisitos").style.display = "none";
        document.getElementById("selMS").style.display = "none";
    }
}