import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

ApplicationWindow {
    visible: true
    width: 500
    height: 400
    Material.theme: "Dark"
    font.pixelSize: 24

    Row {
        id: row
        spacing: 20
        anchors {
            horizontalCenter: parent.horizontalCenter
            top: parent.top
            topMargin: 20
        }
        TextField {
            id: pokemon_id
            placeholderText: "Pokémon ID: "
            width: 200
        }
        Button {
            text: "Search!"
            width: 200
        }
    }
    Label {
        id: label
        text: "Pokémon"
        anchors {
            horizontalCenter: parent.horizontalCenter
            top: row.top
            topMargin: 60
        }
    }
    Image {
        id: img
        width: 300
        height: 300
    }
}