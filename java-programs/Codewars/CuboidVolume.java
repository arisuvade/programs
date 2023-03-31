package Codewars;

public class CuboidVolume {

	public static void main(String[] args) {

		double test1 = getVolumeOfCuboid(5, 2, 3);
		double test2 = getVolumeOfCuboid(6.3, 2, 5);

		System.out.println(test1);
		System.out.println(test2);

	}

	public static double getVolumeOfCuboid(final double length, final double width, final double height) {
		return length * width * height;

	}

}
