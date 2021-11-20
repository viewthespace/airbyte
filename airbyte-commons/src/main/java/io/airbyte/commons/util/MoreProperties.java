package io.airbyte.commons.util;

import com.google.common.collect.Maps;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;

public class MoreProperties {
  public static Properties envFileToProperties(final File file) throws IOException {
    final Properties prop = new Properties();
    prop.load(new FileInputStream(file));
    return prop;
  }
}
