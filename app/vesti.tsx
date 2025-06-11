import React from 'react';
import { Text, View } from "react-native";

export default function App() {
  return (
    <View
      style={{
        flex: 1,
        backgroundColor: '#C6D8AA', 
        justifyContent: "center",
        alignItems: "center",
        borderWidth: 17,
        borderColor: '#8FBE7B',
        borderRadius: 1,
        padding: 1
      }}
    >
      <Text style={{fontFamily: 'Verdana', fontSize: 40, color: '#8A4700'}}>vesti 🌱</Text>
    </View>
  );
}
