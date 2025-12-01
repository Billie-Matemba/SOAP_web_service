# test 1 success msno="01234567890" (success)

curl -X POST https://yourusername.pythonanywhere.com/meter/confirm/ \
  -H "Content-Type: text/xml" \
  -H "SOAPAction: confirmMeter" \
  -d '<?xml version="1.0" ?>
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
    <soap-env:Body>
        <ns0:confirmMeterReq xmlns:ns0="http://www.nrs.eskom.co.za/xmlvend/meter/2.1/schema">
            <ns1:clientID xmlns:ns1="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                id="6004708001981"
                xsi:type="ns1:GenericDeviceID" />
            <ns2:terminalID xmlns:ns2="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                id="00000000000001"
                xsi:type="ns2:GenericDeviceID" />
            <ns3:msgID xmlns:ns3="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                dateTime="22222222222222222"
                uniqueNumber="2222222" />
            <ns0:idMethod>
                <ns4:meterIdentifier xmlns:ns4="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    msno="01234567890"
                    xsi:type="ns4:MeterNumber" />
            </ns0:idMethod>
        </ns0:confirmMeterReq>
    </soap-env:Body>
</soap-env:Envelope>'


# Test 2: Specified Fault (msno="01234567891")
curl -X POST https://yourusername.pythonanywhere.com/meter/confirm/ \
  -H "Content-Type: text/xml" \
  -H "SOAPAction: confirmMeter" \
  -d '<?xml version="1.0" ?>
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
    <soap-env:Body>
        <ns0:confirmMeterReq xmlns:ns0="http://www.nrs.eskom.co.za/xmlvend/meter/2.1/schema">
            <ns1:clientID xmlns:ns1="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                id="6004708001981"
                xsi:type="ns1:GenericDeviceID" />
            <ns2:terminalID xmlns:ns2="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                id="00000000000001"
                xsi:type="ns2:GenericDeviceID" />
            <ns3:msgID xmlns:ns3="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                dateTime="22222222222222222"
                uniqueNumber="2222222" />
            <ns0:idMethod>
                <ns4:meterIdentifier xmlns:ns4="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    msno="01234567891"
                    xsi:type="ns4:MeterNumber" />
            </ns0:idMethod>
        </ns0:confirmMeterReq>
    </soap-env:Body>
</soap-env:Envelope>'


# Test 3: Meter Not Found (msno="01234567892")

curl -X POST https://yourusername.pythonanywhere.com/meter/confirm/ \
  -H "Content-Type: text/xml" \
  -H "SOAPAction: confirmMeter" \
  -d '<?xml version="1.0" ?>
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
    <soap-env:Body>
        <ns0:confirmMeterReq xmlns:ns0="http://www.nrs.eskom.co.za/xmlvend/meter/2.1/schema">
            <ns1:clientID xmlns:ns1="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                id="6004708001981"
                xsi:type="ns1:GenericDeviceID" />
            <ns2:terminalID xmlns:ns2="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                id="00000000000001"
                xsi:type="ns2:GenericDeviceID" />
            <ns3:msgID xmlns:ns3="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                dateTime="22222222222222222"
                uniqueNumber="2222222" />
            <ns0:idMethod>
                <ns4:meterIdentifier xmlns:ns4="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    msno="01234567892"
                    xsi:type="ns4:MeterNumber" />
            </ns0:idMethod>
        </ns0:confirmMeterReq>
    </soap-env:Body>
</soap-env:Envelope>'


# Test 4: Invalid Format (msno="123")

curl -X POST https://yourusername.pythonanywhere.com/meter/confirm/ \
  -H "Content-Type: text/xml" \
  -H "SOAPAction: confirmMeter" \
  -d '<?xml version="1.0" ?>
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
    <soap-env:Body>
        <ns0:confirmMeterReq xmlns:ns0="http://www.nrs.eskom.co.za/xmlvend/meter/2.1/schema">
            <ns1:clientID xmlns:ns1="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                id="6004708001981"
                xsi:type="ns1:GenericDeviceID" />
            <ns2:terminalID xmlns:ns2="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                id="00000000000001"
                xsi:type="ns2:GenericDeviceID" />
            <ns3:msgID xmlns:ns3="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                dateTime="22222222222222222"
                uniqueNumber="2222222" />
            <ns0:idMethod>
                <ns4:meterIdentifier xmlns:ns4="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema"
                    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    msno="123"
                    xsi:type="ns4:MeterNumber" />
            </ns0:idMethod>
        </ns0:confirmMeterReq>
    </soap-env:Body>
</soap-env:Envelope>'