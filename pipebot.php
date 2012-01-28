<?php

/**
 * Class to handle pumping information at pipebot.
 */
class Pipebot
{
	/**
	 * Has pipebot say something, in a manner that doesn't block.
	 * @param message: The string to say.
	 */
	public static function say($message)
	{
		static $s_sayPath;
		if ($s_sayPath == null)
		{
			$s_sayPath = escapeshellarg(dirname(__FILE__).'/say');
		}
		$s_message = escapeshellarg($message);
		shell_exec("$s_sayPath $s_message");
	}
}
