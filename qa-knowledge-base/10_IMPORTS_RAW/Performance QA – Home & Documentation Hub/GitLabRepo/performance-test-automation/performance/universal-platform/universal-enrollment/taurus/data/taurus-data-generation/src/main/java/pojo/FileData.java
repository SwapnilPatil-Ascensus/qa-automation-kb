package pojo;

import java.lang.reflect.Field;

import core.datageneration.data.DataFactory;
import core.datageneration.data.RandomGenerator;
import core.datageneration.data.DataUtility;
import core.datageneration.entity.Person;
import core.datageneration.properties.DateProperties;
import core.datageneration.properties.PersonProperties;

import core.exception.DataGenerationException;

public class FileData {

	private String testCaseName;
	private String ownerFirstName;
	private String ownerLastName;
	private String email;
	private String username;
	private String phone;
	private String ownerSsn;
	private String ownerDob;
	private String address;
	private String city;
	private String beneFirstName;
	private String beneSsn;
	private String beneDob;
	private String bankAcct;
	private String amount;
	private String startDate;
	private String screenshot;

	public void generate() {
		RandomGenerator generator = new RandomGenerator();
		DataFactory factory = new DataFactory();
		Person owner = factory.generatePerson(PersonProperties.withMinAge(21));
		Person beneficiary = factory.generatePerson(PersonProperties.withMaxAge(17));
		
		testCaseName = owner.generateUuid();
		ownerFirstName = owner.getFirstName();
		ownerLastName = owner.getLastName();
		email = owner.getEmail();
		username = owner.getUsername();
		phone = owner.getTelephoneNumber();
		ownerSsn = owner.getSSN();
		ownerDob = owner.getDateOfBirthAsString("MMddyyyy");
		address = owner.getPermanentAddress().getAddressLine1();
		city = owner.getPermanentAddress().getCity();
		beneFirstName = beneficiary.getFirstName();
		beneSsn = beneficiary.getSSN();
		beneDob = beneficiary.getDateOfBirthAsString("MMddyyyy");
		bankAcct = generator.generateRandomDigits(8);
		amount = String.valueOf(generator.generateRandomNumber(250, 1000));
		startDate = DataUtility.convertDateFormat(factory.generateDate(DateProperties.withMonthsYears(true, 1, 0)), "MMddyyyy");
		screenshot = "images\\" + testCaseName + ".jpg";
	}
	
	/**
	 * Get the list of headers (comma delimited)
	 * 
	 * @return Comma delimited list of headers
	 * @throws DataGenerationException Failed to pull headers
	 */
	public String getHeaders() throws DataGenerationException {
		String headers = "";
		try {
			
			//Go through all fields
			for (Field field : this.getClass().getDeclaredFields()) {
				field.setAccessible(true);
				headers += field.getName() + ",";
				field.setAccessible(false);
			}
		} catch (IllegalArgumentException e) {
			throw new DataGenerationException("Failed create data", e);
		}
		
		return headers.substring(0, headers.length() - 1);
	}
	
	/**
	 * Get the list of data (comma delimited)
	 * 
	 * @return Comma delimited list of data
	 * @throws DataGenerationException Failed to pull data
	 */
	public String getData() throws DataGenerationException {
		String headers = "";
		try {
			
			//Go through all fields
			for (Field field : this.getClass().getDeclaredFields()) {
				field.setAccessible(true);
				headers += field.get(this) + ",";
				field.setAccessible(false);
			}
		} catch (IllegalArgumentException | IllegalAccessException e) {
			throw new DataGenerationException("Failed create data", e);
		}
		
		return headers.substring(0, headers.length() - 1);
	}
}
