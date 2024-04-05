// src/components/styled/MessageList.js
import styled from 'styled-components';

const MessageList = styled.div`
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding: 10px;
  flex-grow: 1;
  max-height: 90%; // Adjust as necessary
`;

export default MessageList;
