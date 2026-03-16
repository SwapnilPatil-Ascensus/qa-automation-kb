package runner;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import core.exception.DataGenerationException;
import pojo.FileData;

public class Generator {
	
	public static final Logger logger = LoggerFactory.getLogger(Generator.class);

	public static void main(String[] args) throws IOException, DataGenerationException {
		logger.info("Writing to file... [{} records]", args[0]);
		
		try (BufferedWriter writer = new BufferedWriter(new FileWriter(generateFileName()))) {
			FileData row = new FileData();
			writer.write(row.getHeaders() + "\n");
			writer.flush();
			
			for(int a = 0; a < Integer.parseInt(args[0]); a++) {
				row.generate();
				writer.write(row.getData() + "\n");
				writer.flush();
			}
		}
	}

	/**
	 * Generate a filename
	 * 
	 * @return Generated filename
	 */
	private static String generateFileName() {
		SimpleDateFormat date = new SimpleDateFormat("yyyyMMdd");
		SimpleDateFormat hour = new SimpleDateFormat("HHmmss");
		
		return "data.csv";
	}
}
