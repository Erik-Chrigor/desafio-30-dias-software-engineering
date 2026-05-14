// ---- 1. CAPTURA DE TUDO (O TOPO DO ARQUIVO) ---

const inputDecimal = document.getElementById('numeroDecimal');
const baseSelecionada = document.getElementById('escolhaBase');
const btnBases = document.getElementById('btnConverter');
const resBases = document.getElementById('resultado');

// ENERGIA CINÉTICA --

const inputMassaC = document.getElementById('massa-c');
const inputVelC = document.getElementById('vel-c')
const btnCinetica = document.getElementById('btnCalcularC');
const resCinetica = document.getElementById('res-cinetica');


// ENERGIA POTENCIAL ---

const inputMassaP = document.getElementById('massa-p');
const inputAlturap = document.getElementById('altura-p');
const btnPotencial = document.getElementById('btnCalcularP');
const resPotencial = document.getElementById('res-potencial');


// --- 2 LÒGICA DAS BASES --

btnBases.addEventListener('click', function() {
    let decimal = Number(inputDecimal.value);
    let base = Number(baseSelecionada.value);
    resBases.innerText = `Resultado: ${decimal.toString(base).toUpperCase()}`;
});

// --- 3. LÒGICA DE CINÈTICA ---

btnCinetica.addEventListener('click', function(){
  let m = Number(inputMassaC.value);
  let v = Number(inputVelC.value);
  let ec = (m * (v ** 2 )) / 2;
  resCinetica.innerText = `Energia Cinética: ${ec.toFixed(2)} J`;
});

// --- 4. LÓGICA POTENCIAL --- 

btnPotencial.addEventListener('click', function(){
const g = 9.8;
let m = Number(inputMassaP.value);
let h = Number(inputAlturap.value);
let ep = m * g * h;
resPotencial.innerText = `Energia Potencial: ${ep.toFixed(2)} J`;

});