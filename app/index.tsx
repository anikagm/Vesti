import { useRouter } from 'expo-router';
import React from 'react';
import { Image, Pressable, SafeAreaView, StyleSheet, Text } from 'react-native';
import vestiLogo from '../assets/images/vesti-logo.png';

const VestiWelcomePage = () => {
  const router = useRouter();
  
   return (
    <SafeAreaView style={styles.container}>

      <Text style={{fontFamily: 'Verdana', fontSize: 40, color: '#8A4700', marginBottom: 100}}>
          vesti 🌱
        </Text>

      <Text style={{fontFamily: 'Verdana', fontSize: 24, color: '#8A4700', marginBottom: 20}}>
          enter the barcode image:
        </Text>  

      <SafeAreaView style={styles.buttonShadow} />

      <Pressable style={styles.button} onPress={() => router.push('./results')}>
        <Text style={{fontFamily: 'Verdana', fontSize: 20, color: '#8A4700'}}>upload image</Text>    
      </Pressable>


      <SafeAreaView style={styles.circleWrapper}>
        <SafeAreaView style={styles.circle} />
        <SafeAreaView style={[styles.circle, styles.overlappingCircle]} />
        <Image source={vestiLogo} style={styles.image} />

      </SafeAreaView>

    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-end',
    alignItems: 'center',
    backgroundColor: '#C6D8AA',
    paddingBottom: 100,
    borderWidth: 17,
    borderColor: '#8FBE7B',
    borderRadius: 30
  },
  circleWrapper: {
    width: 200,
    height: 200,
    position: 'relative',
    marginLeft: 22,
  },
  circle: {
    width: 180,
    height: 180,
    borderRadius: 90,
    backgroundColor: '#F4BADC',
    position: 'absolute',
    top: 0,
    left: 0,
  },
  overlappingCircle: {
    top: -6,
    left: -6,
    backgroundColor: '#F7D2E8',
  },
  image: {
    position: 'absolute',
    top: 21,
    left: 20,
    width: 132,
    height: 132,
    resizeMode: 'contain',
  },
  button: {
    marginBottom: 100,
    paddingVertical: 10,
    paddingHorizontal: 20,
    backgroundColor: '#F7D2E8'
  },
  buttonShadow: {
    width: 175,
    height: 40,
    backgroundColor: '#F4BADC',
    position: 'relative',
    top: 50,
    left: 5
  }
});

export default VestiWelcomePage;


