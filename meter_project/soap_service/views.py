from django.shortcuts import render
import re
import logging
from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from defusedxml import defuse_stdlib

# Defuse XML vulnerabilities
defuse_stdlib()

logger = logging.getLogger(__name__)

class MeterSOAPService:
    """Main SOAP service handler."""
    
    @staticmethod
    def extract_meter_number(xml_data):
        """
        Safely extract meter number from SOAP request.
        
        Args:
            xml_data (str): Raw XML request
            
        Returns:
            str: Meter number if found, None otherwise
        """
        try:
            # Use regex to find msno attribute safely
            pattern = r'msno="([^"]+)"'
            match = re.search(pattern, xml_data)
            return match.group(1) if match else None
        except Exception as e:
            logger.error(f"Error extracting meter number: {e}")
            return None
    
    @staticmethod
    def validate_meter_number(msno):
        """
        Validate meter number format.
        
        Args:
            msno (str): Meter number
            
        Returns:
            tuple: (is_valid, error_message)
        """
        if not msno:
            return False, "Meter number is required"
        
        if not msno.isdigit():
            return False, "Meter number must contain only digits"
        
        if len(msno) != 11:
            return False, "Invalid Meter Number Format"
        
        return True, ""
    
    @staticmethod
    def get_response_for_meter(msno):
        """
        Get appropriate SOAP response based on meter number.
        
        Args:
            msno (str): Meter number
            
        Returns:
            str: SOAP XML response
        """
        from .soap_templates import (
            get_success_template,
            get_specific_fault_template,
            get_meter_not_found_template,
            get_soap_fault_template
        )
        
        # Special cases
        if msno == "01234567891":
            return get_specific_fault_template()
        elif msno == "01234567892":
            return get_meter_not_found_template()
        
        # Validate format
        is_valid, error_msg = MeterSOAPService.validate_meter_number(msno)
        if is_valid:
            timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+02:00')
            return get_success_template(msno, timestamp)
        else:
            return get_soap_fault_template(error_msg)

@require_POST
@csrf_exempt
def meter_confirmation_endpoint(request):
    """
    SOAP endpoint for meter confirmation.
    Exposed at: /meter/confirm/
    """
    try:
        # Log request for debugging
        logger.info(f"Received SOAP request from {request.META.get('REMOTE_ADDR')}")
        
        # Read and decode XML data
        xml_data = request.body.decode('utf-8', errors='ignore')
        
        # Extract meter number
        msno = MeterSOAPService.extract_meter_number(xml_data)
        
        if not msno:
            logger.warning("No meter number found in request")
            from .soap_templates import get_soap_fault_template
            response_xml = get_soap_fault_template("Invalid request: No meter number found")
            return HttpResponse(response_xml, content_type='text/xml; charset=utf-8', status=400)
        
        logger.info(f"Processing meter number: {msno}")
        
        # Get appropriate response
        response_xml = MeterSOAPService.get_response_for_meter(msno)
        
        # Return SOAP response
        return HttpResponse(response_xml, content_type='text/xml; charset=utf-8')
        
    except Exception as e:
        logger.error(f"Unexpected error processing SOAP request: {e}")
        from .soap_templates import get_soap_fault_template
        response_xml = get_soap_fault_template(f"Internal server error: {str(e)}")
        return HttpResponse(response_xml, content_type='text/xml; charset=utf-8', status=500)