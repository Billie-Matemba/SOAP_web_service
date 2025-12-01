"""
SOAP XML response templates for the meter confirmation service.
"""

def get_success_template(msno, timestamp):
    """Template for successful meter confirmation."""
    return f'''<?xml version='1.0' encoding='UTF-8'?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <confirmMeterResp xmlns:b0="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema" xmlns:r0="http://www.nrs.eskom.co.za/xmlvend/revenue/2.1/schema" xmlns="http://www.nrs.eskom.co.za/xmlvend/meter/2.1/schema">
            <b0:clientID xsi:type="b0:GenericDeviceID" id="6004708000090"/>
            <b0:serverID xsi:type="b0:EANDeviceID" ean="0123123456789"/>
            <b0:terminalID xsi:type="b0:GenericDeviceID" id="6004708000090"/>
            <b0:reqMsgID dateTime="222222222222222" uniqueNumber="2222222"/>
            <b0:respDateTime>{timestamp}</b0:respDateTime>
            <b0:dispHeader>Confirm Meter Details</b0:dispHeader>
            <confirmMeterResult>
                <meterDetail xsi:type="b0:ExtMeterDetail" msno="{msno}" sgc="100836" km="2" ti="07">
                    <b0:meterType at="07" tt="02"/>
                </meterDetail>
            </confirmMeterResult>
        </confirmMeterResp>
    </soap:Body>
</soap:Envelope>'''

def get_specific_fault_template():
    """Template for specific fault (msno=01234567891)."""
    return '''<?xml version='1.0' encoding='UTF-8'?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <soap:Fault>
            <faultcode>soap:Server</faultcode>
            <faultstring>010038 Meter information not found</faultstring>
            <faultactor>http://onlinewending.eskom.co.za/OVS/WS/Actaris.WSNRS21EskomFull/WSactaris.asmx</faultactor>
            <detail>
                <b0:xmlvendFaultResp xmlns:b0="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema">
                    <b0:clientID xmlns:d3p1="http://www.w3.org/2001/XMLSchema-instance" d3p1:type="b0:GenericDeviceID" id="6004708000090"/>
                    <b0:serverID xmlns:d3p1="http://www.w3.org/2001/XMLSchema-instance" d3p1:type="b0:EANDeviceID" ean="0123123456789"/>
                    <b0:terminalID xmlns:d3p1="http://www.w3.org/2001/XMLSchema-instance" d3p1:type="b0:GenericDeviceID" id="6004708000090"/>
                    <b0:reqMsgID dateTime="22222222222222222" uniqueNumber="2222222"/>
                    <b0:respDateTime>2025-07-08T16:55:55.739+02:00</b0:respDateTime>
                    <b0:dispHeader>ONLINE ERROR</b0:dispHeader>
                    <b0:operatorMsg>Meter information not found,cannot process request. Contact Eskom to register meter</b0:operatorMsg>
                    <b0:custMsg>Meter not found.Contact Eskom to register meter</b0:custMsg>
                    <b0:fault xmlns:d3p1="http://www.w3.org/2001/XMLSchema-instance" d3p1:type="b0:UnknownMeterEx">
                        <b0:desc>010038 Meter information not found</b0:desc>
                    </b0:fault>
                </b0:xmlvendFaultResp>
            </detail>
        </soap:Fault>
    </soap:Body>
</soap:Envelope>'''

def get_meter_not_found_template():
    """Template for meter not found response (msno=01234567892)."""
    return '''<?xml version='1.0' encoding='UTF-8'?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <confirmMeterResp xmlns:b0="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema" xmlns:r0="http://www.nrs.eskom.co.za/xmlvend/revenue/2.1/schema" xmlns="http://www.nrs.eskom.co.za/xmlvend/meter/2.1/schema">
            <b0:clientID xsi:type="b0:GenericDeviceID" id="6004708000090"/>
            <b0:serverID xsi:type="b0:EANDeviceID" ean="0123123456789"/>
            <b0:terminalID xsi:type="b0:GenericDeviceID" id="6004708000090"/>
            <b0:reqMsgID dateTime="22222222222222222" uniqueNumber="2222222"/>
            <b0:respDateTime>2025-07-08T16:55:55.739+02:00</b0:respDateTime>
            <b0:dispHeader>METER NOT FOUND</b0:dispHeader>
            <confirmMeterResult>
                <meterNotFound>Meter not Found</meterNotFound>
            </confirmMeterResult>
        </confirmMeterResp>
    </soap:Body>
</soap:Envelope>'''

def get_soap_fault_template(error_message):
    """Template for generic SOAP fault responses."""
    return f'''<?xml version='1.0' encoding='UTF-8'?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <soap:Fault>
            <faultcode>soap:Server</faultcode>
            <faultstring>{error_message}</faultstring>
        </soap:Fault>
    </soap:Body>
</soap:Envelope>'''