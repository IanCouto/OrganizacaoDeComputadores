a = ""


def __init__(self):
    a = "a"


def traduzirComando(str):
    """if(pc > enderecoFinalInstrucoes){
      resetImagem()
      $("#instrucaoAtual").html("Finalizado")
      return 0
    }
    """
    opcode = str[26:32]
    rs = str[21:26]
    rt = str[16:21]
    rd = str[11:16]
    sa = str[6:11]
    func = str[0:6]
    immediate = str[0:16]
    desvio = str[0:26]
    if(func in dicComandosR):
      print(dicComandosR[func], dicRegistradores[rs], dicRegistradores[rt], dicRegistradores[rd])
    elif(func in dicComandosIJ):
      print(dicComandosIJ[func], dicRegistradores[rs], dicRegistradores[rt], dicRegistradores[rd])
"""
  if (opcode == 0) {
    #Tipo R
    switch (func) {
      case 0: #sll
        instrucaoTraduzida =
          dicComandosR[func] +
          " " +
          dicRegistradores[rd] +
          ", " +
          dicRegistradores[rt] +
          ", " +
          sa;
        break;

      case 8: #jr
        instrucaoTraduzida = dicComandosR[func] + " " + dicRegistradores[rs];
        break;

      default:
        #Tipo R qualquer
        instrucaoTraduzida =
          dicComandosR[func] +
          " " +
          dicRegistradores[rd] +
          ", " +
          dicRegistradores[rs] +
          ", " +
          dicRegistradores[rt];
        break;
    }
    
    $("."+instrucaoAnterior).css("stroke","black")
    $("."+dicComandosR[func]).css("stroke","red")
    instrucaoAnterior = dicComandosR[func]

  } 
  else {
    switch (opcode) {
      case 2:
      case 3: #tipo J
        instrucaoTraduzida = dicComandosIJ[opcode] + " " + desvio;
        break;

      case 35:
      case 43: #lw e sw
        instrucaoTraduzida =
          dicComandosIJ[opcode] +
          " " +
          dicRegistradores[rt] +
          ", " +
          immediate +
          "(" +
          dicRegistradores[rs] +
          ")";
        break;

      case 4:
      case 5: #beq e bne
        instrucaoTraduzida =
          dicComandosIJ[opcode] +
          " " +
          dicRegistradores[rs] +
          ", " +
          dicRegistradores[rt] +
          ", " +
          immediate;
        break;

      default:
        #Tipo I qualquer
        instrucaoTraduzida =
          dicComandosIJ[opcode] +
          " " +
          dicRegistradores[rt] +
          ", " +
          dicRegistradores[rs] +
          ", " +
          immediate;
        break;
    }
    
    $("."+instrucaoAnterior).css("stroke","black")
    $("."+dicComandosIJ[opcode]).css("stroke","red")
    instrucaoAnterior = dicComandosIJ[opcode]
  }

  $("#instrucaoAtual").html(instrucaoTraduzida);
  
}
"""
dicComandosR = {
    '100000': "add",
    '100010': "sub",
    '011000': "mult",
    '011010': "div",
    '100100': "and",
    '100101': "or",
    '101010': "slt",
    '000000': "sll",
    '001000': "jr",
}

dicComandosIJ = {
    '001000': "addi",
    '100011': "lw",
    '101011': "sw",
    '000100': "beq",
    '000101': "bne",
    '000010': "j",
    '000011': "jal",
}

dicRegistradores = {
    '00000': "$zero",
    '00001': "$at",
    '00010': "$v0",
    '00011': "$v1",
    '00100': "$a0",
    '00101': "$a1",
    '00110': "$a2",
    '00111': "$a3",
    '01000': "$t0",
    '01001': "$t1",
    '01010': "$t2",
    '01011': "$t3",
    '01100': "$t4",
    '01101': "$t5",
    '01110': "$t6",
    '01111': "$t7",
    '10000': "$s0",
    '10001': "$s1",
    '10010': "$s2",
    '10011': "$s3",
    '10100': "$s4",
    '10101': "$s5",
    '10110': "$s6",
    '10111': "$s7",
    '11000': "$t8",
    '11001': "$t9",
    '11010': "$k0",
    '11011': "$k1",
    '11100': "$gp",
    '11101': "$sp",
    '11110': "$fp",
    '11111': "$ra",
}