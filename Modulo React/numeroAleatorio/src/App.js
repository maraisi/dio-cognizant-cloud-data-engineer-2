import React, {useState} from "react";
import {View, Text, SafeAreaView, TouchableOpacity, StyleSheet} from 'react-native'

const App = () => {
  return (
    /* so pode retornar um componente. 
    Caso seja necessario, usar fragment <> </> */
    <SafeAreaView style={style.container}>
      <Text style={style.numero}>0</Text>
      <TouchableOpacity style={style.botao}>
        <Text>Gerar Número</Text>
      </TouchableOpacity>
    </SafeAreaView>
  );
};

const style = StyleSheet.create({
  container: {
    background: 'red',
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  numero: {
    fontSize: 38,
    color: '#FFFFFF',
    fontWeight: 'bold',
  },
  botao: {
    background: '#FFFFFF',
    width: '100%',
    paddingHorizontal: 10,
    paddingVertical:25,
    borderRadius: 5,
    justifyContent: 'center',
    alignContent: 'center',
    marginTop: 10
  },


});

export default App;