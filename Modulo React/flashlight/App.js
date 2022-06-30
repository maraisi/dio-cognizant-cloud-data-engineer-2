import React, {useState, useEffect} from 'react';
import {View, StyleSheet, Image, TouchableOpacity, Alert} from 'react-native';
import Torch from 'react-native-torch';
import RNShake from 'react-native-shake';

//import imagex from './assets/icons/eco-light.png'

const App = () =>{
  const [toggle, setToggle] = useState(false);
  
  const handChangeToggle = () => setToggle(oldToggle => !oldToggle);


  useEffect(() => {
    //liga o flash
    //Alert.alert("Atualizou o componente " + toggle);
    Torch.switchState(toggle);
  },[toggle]);


  useEffect(()=>{
    /* O toggle é mudado quando celular for chacoalhar */
    const subscription = RNShake.addListener(()=>{
      setToggle(oldToggle => !oldToggle);
    });

    //função chamada quando o componentefor desmontado
    return ()=> subscription.remove();
  }, []);

  // if ternário
  return(
    <View style={toggle ? style.constainerLight : style.constainer}>
      
      <TouchableOpacity onPress= {handChangeToggle}>

        
        <Image 
          style={toggle ? style.lightningOn : style.lightningOff}
          source={
            toggle 
              ? require('./assets/icons/eco-light.png')
              : require('./assets/icons/eco-light-off.png')
            }

      
        />
        <Image 
          style={style.dioLogo}
          source={
            toggle 
              ? require('./assets/icons/logo-dio.png')
              : require('./assets/icons/logo-dio-white.png')
            }

      
        />
      </TouchableOpacity>
    </View>
    
      
  );

};

export default App;

const style = StyleSheet.create({
  constainer:{
    flex: 1,
    background: 'black',
    alignItems: 'center',
    justifyContent: 'center',
  },

  constainerLight:{
    flex: 1,
    background: 'white',
    alignItems: 'center',
    justifyContent: 'center',
  },

  lightningOn:{
    resizeMode: 'contain',
    alignSelf: 'center',
    width: 150,
    height: 150,
  },
  
  lightningOff:{
    resizeMode: 'contain',
    alignSelf: 'center',
    width: 150,
    height: 150,
    tintColor: 'white',
  },
  
  dioLogo:{
    resizeMode: 'contain',
    alignSelf: 'center',
    width: 150,
    height: 150,
  },
  

});
