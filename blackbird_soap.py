import requests
import blackbird_prescript as bp

def soap_request(oid):

    nonce = bp.generateNonce()
    secret, nonce, timestamp = bp.generateAmadeusSOAPPassword()


    payload = f'''<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Header>
            <add:MessageID xmlns:add="http://www.w3.org/2005/08/addressing">870c1758-047d-84bc-123f-e5bd5e02ffd8</add:MessageID>
            <add:Action xmlns:add="http://www.w3.org/2005/08/addressing">http://webservices.amadeus.com/TSRQRQ_17_1_1A</add:Action>
            <add:To xmlns:add="http://www.w3.org/2005/08/addressing">https://nodeD1.production.webservices.amadeus.com/1ASIWFCT1FS</add:To>
            <link:TransactionFlowLink xmlns:link="http://wsdl.amadeus.com/2010/06/ws/Link_v1"/>
            <oas:Security xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
                <oas:UsernameToken oas1:Id="UsernameToken-1" xmlns:oas1="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                    <oas:Username>{bp.USERNAME}</oas:Username>
                    <oas:Nonce EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary">{nonce}</oas:Nonce>
                    <oas:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest">{secret}</oas:Password>
                    <oas1:Created>{timestamp}</oas1:Created>
                </oas:UsernameToken>
            </oas:Security>
            <AMA_SecurityHostedUser xmlns="http://xml.amadeus.com/2010/06/Security_v1">
                <UserID POS_Type="1" PseudoCityCode="{oid}" AgentDutyCode="SU" RequestorType="U"/>
            </AMA_SecurityHostedUser>
        </soap:Header>
        <soap:Body>
            <SalesReports_DisplayQueryReport>
                <agencyDetails>
                    <sourceType>
                        <sourceQualifier1>REP</sourceQualifier1>
                    </sourceType>
                    <originatorDetails>
                        <inHouseIdentification1>{oid}</inHouseIdentification1>
                    </originatorDetails>
                </agencyDetails>
                <salesPeriodDetails>
                    <beginDateTime>
                        <year>2023</year>
                        <month>03</month>
                        <day>23</day>
                    </beginDateTime>
                    <endDateTime>
                        <year>2023</year>
                        <month>03</month>
                        <day>23</day>
                    </endDateTime>
                </salesPeriodDetails>
                <requestOption>
                    <selectionDetails>
                        <option>SOF</option>
                    </selectionDetails>
                </requestOption>
            </SalesReports_DisplayQueryReport>
        </soap:Body>
    </soap:Envelope>'''

    headers = {
    'SOAPAction': 'http://webservices.amadeus.com/TSRQRQ_17_1_1A',
    'Content-Type': 'text/xml'
    }

    response = requests.post(bp.url, headers=headers, data=payload)

    return response