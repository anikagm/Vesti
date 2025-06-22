import React, { useState } from 'react';
import { Pressable, SafeAreaView, StyleSheet, Text } from 'react-native';


const VestiResultsPage = () => {
  const [showText, setShowText] = useState(false);

   return (
    <SafeAreaView style={styles.container}>

      <SafeAreaView style={styles.buttonShadow} />

      <Pressable style={styles.button} onPress={() => setShowText(!showText)}>
        <Text style={{fontFamily: 'Verdana', fontSize: 15, color: '#8A4700'}}>Click to explore sustainability info:</Text>    
      </Pressable>
      {showText ? <Text style={{fontFamily: 'Verdana', fontSize: 15, color: '#8A4700'}}>Here are the results</Text> : null}

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
    marginBottom: 20,
    paddingVertical: 10,
    paddingHorizontal: 20,
    backgroundColor: '#F7D2E8'
  },
  buttonShadow: {
    width: 300,
    height: 40,
    backgroundColor: '#F4BADC',
    position: 'relative',
    top: 45,
    left: 5
  }
});

export default VestiResultsPage;

