import React from 'react';
import { Image, SafeAreaView, StyleSheet, Text } from 'react-native';
import vestiLogo from '../assets/images/vesti-logo.png';

const VestiWelcomePage= () => {
  return (
    <SafeAreaView style={styles.container}>
      <SafeAreaView style={styles.circleWrapper}>
        <SafeAreaView style={styles.circle} />
        <SafeAreaView style={[styles.circle, styles.overlappingCircle]} />
        <Image source={vestiLogo} style={styles.image} />
        <Text style={{ fontSize: 24, color: '#8A4700', marginBottom: 100, position: 'absolute', top: -250, left: -30, width: 500}}>Enter the barcode image:</Text>    
      <Text style={{fontFamily: 'Verdana', fontSize: 40, color: '#8A4700', position: 'absolute', top: -400, left: 30}}>vesti 🌱</Text>
      </SafeAreaView>
    </SafeAreaView>
  );
};

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
});

export default VestiWelcomePage;

