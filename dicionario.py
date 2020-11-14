a = ""
def __init__(self):
  a = "a"

def traduzirComando(memoria):
  """if(pc > enderecoFinalInstrucoes){
    resetImagem()
    $("#instrucaoAtual").html("Finalizado")
    return 0
  }
  """
  opcode = str(memoria.get(0))[26:31]
  rs = str(memoria.get(0))[21:25]
  rt = str(memoria.get(0))[16:20]
  rd = str(memoria.get(0))[12:12]
  sa = str(memoria.get(0))[6:10]
  func = str(memoria.get(0))[0:5]
  immediate = str(memoria.get(0))[0:15]
  desvio = str(memoria.get(0))[0:25]
  print("5")

    

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
    '00100000': "add",
    '00100010': "sub",
    '00011000': "mult",
    '00011010': "div",
    '00100100': "and",
    '00100101': "or",
    '00101010': "slt",
    '00000000': "sll",
    '00001000': "jr",
}

dicComandosIJ = {
    '00001000': "addi",
    '00100011': "lw",
    '00101011': "sw",
    '00000100': "beq",
    '00000101': "bne",
    '00000010': "j",
    '00000011': "jal",
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
