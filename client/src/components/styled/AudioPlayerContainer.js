import styled from 'styled-components';

const AudioPlayerContainer = styled.div`
  width: 100%;
  height: 40px;
  margin: 5px 0; // Adjust margin as needed to fit your design

  audio {
    width: 50%; // Ensures audio player is not shrinking
    height: 100%; // Adjust height as necessary
  }
`;

export default AudioPlayerContainer;
