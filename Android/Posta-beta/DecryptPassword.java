public class DecryptPassword {
    public static void main(String[] args) {
        byte[] SEC_BYTES = {32, 60, 46, 28, 80, 3, 49, 2, 3, 24, 4, 113, 18, 92, 7, 64, 62, 85, 90, 89, 28, 4, 72, 2, 94, 72, 8, 86, 72, 21, 18};
        String packageName = "com.example.posta";
        
        try {
            byte[] ccskey = packageName.getBytes("ASCII");
            byte[] decrypted = new byte[SEC_BYTES.length];
            
            for (int i = 0; i < SEC_BYTES.length; i++) {
                decrypted[i] = (byte) (SEC_BYTES[i] ^ ccskey[i % ccskey.length]);
            }
            
            System.out.println("Decrypted password: " + new String(decrypted, "ASCII").trim());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}